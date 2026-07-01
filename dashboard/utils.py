from datetime import datetime


def format_number(value):
    return f"{value:,.0f}"


def format_currency(value):
    return f"${value:,.2f}"


def format_percentage(value):
    return f"{value:.2f}%"


def format_date(date_value):
    if isinstance(date_value, datetime):
        return date_value.strftime("%Y-%m-%d")
    return str(date_value)


def apply_whatif_adjustment(forecast_df, adjustment_pct):
    adjusted = forecast_df.copy()
    multiplier = 1 + (adjustment_pct / 100)
    adjusted["yhat"] = adjusted["yhat"] * multiplier
    adjusted["yhat_lower"] = adjusted["yhat_lower"] * multiplier
    adjusted["yhat_upper"] = adjusted["yhat_upper"] * multiplier
    return adjusted