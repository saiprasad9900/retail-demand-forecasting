from dashboard.data_loader import (
    load_forecast_results,
    load_actual_vs_predicted,
    load_forecast_summary,
)
from dashboard.filters import filter_by_date, get_date_range
from dashboard.metrics import get_model_metrics, get_forecast_kpis
from dashboard.utils import apply_whatif_adjustment


def get_dashboard_data(start_date=None, end_date=None):
    forecast = load_forecast_results()
    actual_vs_predicted = load_actual_vs_predicted()

    if start_date and end_date:
        forecast = filter_by_date(forecast, start_date, end_date)
        actual_vs_predicted = filter_by_date(actual_vs_predicted, start_date, end_date)

    return forecast, actual_vs_predicted


def get_metrics():
    summary = load_forecast_summary()
    return get_model_metrics(summary)


def get_kpis(start_date=None, end_date=None):
    forecast, _ = get_dashboard_data(start_date, end_date)
    return get_forecast_kpis(forecast)


def get_whatif_data(adjustment_pct, start_date=None, end_date=None):
    forecast, _ = get_dashboard_data(start_date, end_date)
    return apply_whatif_adjustment(forecast, adjustment_pct)


def get_date_bounds():
    forecast = load_forecast_results()
    return get_date_range(forecast)