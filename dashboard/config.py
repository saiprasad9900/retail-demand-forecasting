from pathlib import Path

# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Processed data folder
DATA_FOLDER = BASE_DIR / "data" / "processed"

# CSV files
FORECAST_RESULTS = DATA_FOLDER / "forecast_results.csv"
FORECAST_OUTPUT = DATA_FOLDER / "forecast_output.csv"
ACTUAL_VS_PREDICTED = DATA_FOLDER / "actual_vs_predicted.csv"
FORECAST_SUMMARY = DATA_FOLDER / "forecast_summary.csv"