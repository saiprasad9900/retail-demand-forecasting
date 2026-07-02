from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from dashboard.services import (
    get_dashboard_data,
    get_date_bounds,
    get_kpis,
    get_metrics,
    get_whatif_data,
)
from dashboard.utils import format_date, format_number, format_percentage

st.set_page_config(page_title="Retail Demand Forecasting", page_icon="📈", layout="wide")


@st.cache_data(show_spinner=False)
def load_weekly_sales_data():
    weekly_sales_path = Path("dbt/outputs/weekly_sales.csv")
    if not weekly_sales_path.exists():
        return pd.DataFrame(columns=["week_start", "total_sales", "day_count"])

    weekly_sales = pd.read_csv(weekly_sales_path)
    weekly_sales["week_start"] = pd.to_datetime(weekly_sales["week_start"])
    return weekly_sales.sort_values("week_start")


st.markdown("<h1 style='margin-bottom:0;'>M5 Retail Sales Forecasting Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:16px; color:#475569; margin-top:0;'>Forecast future retail demand from historical sales patterns to support inventory planning, reduce stock shortages, and avoid overstocking.</p>", unsafe_allow_html=True)

st.markdown("### Business Objective")
st.write("This solution estimates future demand from historical sales data so retail teams can make informed decisions around inventory, replenishment, and supply chain planning.")

st.markdown("### Decision Support Areas")
objective_col1, objective_col2, objective_col3 = st.columns(3)
with objective_col1:
    st.markdown("**Inventory Planning**")
    st.write("Maintain balanced stock levels and reduce excess inventory.")
with objective_col2:
    st.markdown("**Stockout Prevention**")
    st.write("Anticipate demand spikes and minimize shortages.")
with objective_col3:
    st.markdown("**Supply Chain Operations**")
    st.write("Support replenishment planning and operational readiness.")

st.markdown("### Business Summary")
summary_col1, summary_col2, summary_col3 = st.columns(3)
with summary_col1:
    st.metric("Demand Outlook", "Moderate", help="Overall trend based on the selected forecast window.")
with summary_col2:
    st.metric("Inventory Risk", "Monitor", help="Watch for potential shortages or excess inventory based on forecast movement.")
with summary_col3:
    st.metric("Planning Focus", "Replenishment", help="Prioritize replenishment and stock balancing for the next forecast period.")

st.markdown("### Recommended Actions")
recommended_actions = [
    "Review stock levels for high-demand items before the next replenishment cycle.",
    "Monitor forecast volatility and adjust safety stock where demand is unstable.",
    "Use the what-if adjustment to simulate demand scenarios for better planning."
]
for action in recommended_actions:
    st.write(f"- {action}")

start_date, end_date = get_date_bounds()

with st.sidebar:
    st.header("Filters")
    selected_start = st.date_input("Start date", value=start_date, min_value=start_date, max_value=end_date)
    selected_end = st.date_input("End date", value=end_date, min_value=selected_start, max_value=end_date)

    if selected_start > selected_end:
        st.error("Start date must be before or equal to end date.")
        st.stop()

    adjustment_pct = st.slider("What-if adjustment (%)", min_value=-30, max_value=30, value=0, step=5)
    st.caption("Apply a percentage uplift or reduction to the forecast values.")

try:
    forecast_df, actual_df = get_dashboard_data(str(selected_start), str(selected_end))
    metrics = get_metrics()
    kpis = get_kpis(str(selected_start), str(selected_end))

    if adjustment_pct != 0:
        forecast_df = get_whatif_data(adjustment_pct, str(selected_start), str(selected_end))

    forecast_df = forecast_df.sort_values("date")
    actual_df = actual_df.sort_values("date")

    forecast_df = forecast_df.tail(30).copy()
    actual_df = actual_df[actual_df["date"].isin(forecast_df["date"])].copy()
except Exception as exc:
    st.error(f"Unable to load dashboard data: {exc}")
    st.stop()

forecast_end_date = forecast_df["date"].max()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Next 30-Day Forecast Sales", format_number(forecast_df["yhat"].sum()))
with col2:
    st.metric("Average Daily Forecast", format_number(forecast_df["yhat"].mean()))
with col3:
    st.metric("Forecast End Date", format_date(forecast_end_date))
with col4:
    st.metric("Highest Forecast Day", format_date(forecast_df.loc[forecast_df["yhat"].idxmax(), "date"]))

col5, col6, col7 = st.columns(3)
with col5:
    st.metric("MAE", format_number(metrics.get("MAE", 0)))
with col6:
    st.metric("RMSE", format_number(metrics.get("RMSE", 0)))
with col7:
    st.metric("MAPE", format_percentage(metrics.get("MAPE", 0)))

st.markdown("---")
st.markdown("## Executive Forecast View")
st.info("This section highlights the projected sales trend for the upcoming period, helping teams evaluate likely demand and plan operations accordingly.")

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=forecast_df["date"],
        y=forecast_df["yhat"],
        mode="lines+markers",
        name="Forecast",
        line=dict(color="#2563eb", width=3),
    )
)
fig.add_trace(
    go.Scatter(
        x=forecast_df["date"],
        y=forecast_df["yhat_lower"],
        mode="lines",
        name="Lower bound",
        line=dict(color="#93c5fd", dash="dash"),
    )
)
fig.add_trace(
    go.Scatter(
        x=forecast_df["date"],
        y=forecast_df["yhat_upper"],
        mode="lines",
        name="Upper bound",
        line=dict(color="#93c5fd", dash="dash"),
    )
)
fig.add_trace(
    go.Scatter(
        x=actual_df["date"],
        y=actual_df["actual_sales"],
        mode="markers",
        name="Actual sales",
        marker=dict(color="#dc2626", size=6),
    )
)
fig.update_layout(
    title="Forecast vs Actual Sales",
    xaxis_title="Date",
    yaxis_title="Sales",
    legend_title="Series",
    template="plotly_white",
    margin=dict(l=20, r=20, t=50, b=20),
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("### Error Analysis")
error_chart = go.Figure()
error_chart.add_trace(
    go.Scatter(
        x=actual_df["date"],
        y=actual_df["error"],
        mode="lines+markers",
        name="Prediction error",
        line=dict(color="#7c3aed"),
    )
)
error_chart.update_layout(
    title="Daily Forecast Error",
    xaxis_title="Date",
    yaxis_title="Error",
    template="plotly_white",
    margin=dict(l=20, r=20, t=50, b=20),
)
st.plotly_chart(error_chart, use_container_width=True)

st.markdown("### Weekly Sales Output")
weekly_sales = load_weekly_sales_data()
if weekly_sales.empty:
    st.info("The weekly sales output file is not available yet.")
else:
    weekly_fig = go.Figure()
    weekly_fig.add_trace(
        go.Scatter(
            x=weekly_sales["week_start"],
            y=weekly_sales["total_sales"],
            mode="lines+markers",
            name="Weekly sales",
            line=dict(color="#0f766e", width=2),
        )
    )
    weekly_fig.update_layout(
        title="Weekly Sales Trend from dbt Output",
        xaxis_title="Week Start",
        yaxis_title="Sales",
        template="plotly_white",
        margin=dict(l=20, r=20, t=50, b=20),
    )
    st.plotly_chart(weekly_fig, use_container_width=True)

st.markdown("### Forecast Data")
forecast_table = forecast_df[["date", "yhat", "yhat_lower", "yhat_upper", "total_sales"]].copy()
forecast_table["yhat"] = forecast_table["yhat"].map(lambda x: f"{x:,.0f}")
forecast_table["yhat_lower"] = forecast_table["yhat_lower"].map(lambda x: f"{x:,.0f}")
forecast_table["yhat_upper"] = forecast_table["yhat_upper"].map(lambda x: f"{x:,.0f}")
forecast_table["total_sales"] = forecast_table["total_sales"].map(lambda x: f"{x:,.0f}")
st.dataframe(forecast_table, use_container_width=True)
