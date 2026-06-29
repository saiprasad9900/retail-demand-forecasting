import pandas as pd

from dashboard.config import (
    FORECAST_RESULTS,
    FORECAST_OUTPUT,
    ACTUAL_VS_PREDICTED,
    FORECAST_SUMMARY,
)
def load_forecast_results():
    forecast_df = pd.read_csv(FORECAST_RESULTS)

    forecast_df["date"] = pd.to_datetime(forecast_df["date"])

    return forecast_df
def load_actual_vs_predicted():
    comparison_df = pd.read_csv(ACTUAL_VS_PREDICTED)

    comparison_df["date"] = pd.to_datetime(comparison_df["date"])

    return comparison_df
def load_forecast_summary():
    summary_df = pd.read_csv(FORECAST_SUMMARY)

    return summary_df


def load_forecast_output():
    output_df = pd.read_csv(FORECAST_OUTPUT)

    output_df["ds"] = pd.to_datetime(output_df["ds"])

    return output_df