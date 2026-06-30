import pandas as pd


def filter_by_date(dataframe, start_date, end_date):
    """
    Filter forecast data between two dates.
    """

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    filtered_dataframe = dataframe[
        (dataframe["date"] >= start_date) &
        (dataframe["date"] <= end_date)
    ]

    filtered_dataframe = filtered_dataframe.copy()

    return filtered_dataframe