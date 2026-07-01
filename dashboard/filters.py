import pandas as pd


def filter_by_date(dataframe, start_date, end_date):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    filtered_dataframe = dataframe[
        (dataframe["date"] >= start_date) &
        (dataframe["date"] <= end_date)
    ]

    return filtered_dataframe.copy()


def get_date_range(df, date_col="date"):
    df[date_col] = pd.to_datetime(df[date_col])
    return df[date_col].min(), df[date_col].max()