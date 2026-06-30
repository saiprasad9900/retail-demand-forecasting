import pandas as pd


def get_model_metrics(summary_dataframe):
    """
    Return the model evaluation metrics.
    """
    metrics = {}

    for _, row in summary_dataframe.iterrows():
        metrics[row["Metric"]] = row["Value"]

    return metrics


def get_forecast_kpis(forecast_dataframe):
    """
    Return business KPIs from the forecast results.
    """

    total_forecast_sales = float(forecast_dataframe["yhat"].sum())

    average_daily_forecast = float(forecast_dataframe["yhat"].mean())

    highest_day = forecast_dataframe.loc[
        forecast_dataframe["yhat"].idxmax()
    ]

    lowest_day = forecast_dataframe.loc[
        forecast_dataframe["yhat"].idxmin()
    ]

    highest_forecast_sales = float(highest_day["yhat"])

    lowest_forecast_sales = float(lowest_day["yhat"])

    return {
        "total_forecast_sales": total_forecast_sales,
        "average_daily_forecast": average_daily_forecast,
        "highest_forecast_day": highest_day["date"],
        "highest_forecast_sales": highest_forecast_sales,
        "lowest_forecast_day": lowest_day["date"],
        "lowest_forecast_sales": lowest_forecast_sales,
    }