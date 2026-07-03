# M5 Retail Sales Forecasting Project

## Project Overview
This project builds an end-to-end retail sales forecasting workflow using the Kaggle M5 Forecasting Dataset. The goal is to analyze historical Walmart sales data, uncover business insights, engineer features, and generate forecasts that support demand planning and inventory decisions.

## Business Problem
Retail companies need reliable demand forecasts to:
- maintain optimal inventory levels
- reduce stock shortages
- avoid overstocking
- improve supply chain planning
- increase revenue
- reduce operational costs

## Project Goals
- analyze historical sales patterns and trends
- build a forecasting model for future demand
- create an interactive dashboard for business users
- provide forecast outputs that support planning decisions

---

# Week 3 Complete Summary: Prophet Forecasting Pipeline

## What Was Accomplished in Week 3

### COMMIT 1: Data Validation & Train/Test Split (Day 1)
✅ **Responsibilities:**
- Validated features_engineered_complete.csv (1913 rows × 31 columns)
- Created time-based train/test split (70/30)
- Created feature reference documentation

✅ **Deliverables:**
- data/processed/train_data.csv (1,339 rows)
- data/processed/test_data.csv (574 rows)
- reports/data_validation_report.md
- reports/feature_reference.md

---

### COMMIT 2: Prophet Model Training (Day 2)
✅ **Responsibilities:**
- Trained Prophet on training data (Google Colab)
- Generated 30-day forecasts (574 days test period)
- Created forecast with confidence intervals

✅ **Deliverables:**
- data/processed/forecast_output.csv (574 rows × 4 columns)
- notebooks/week3_prophet_colab.ipynb

---

### COMMIT 3: Model Evaluation & Metrics (Day 3)
✅ **Responsibilities:**
- Calculated evaluation metrics (MAE, RMSE, MAPE)
- Created forecast vs actual visualizations
- Generated model evaluation report

✅ **Deliverables:**
- data/processed/forecast_results.csv (574 rows - forecast + actual merged)
- data/processed/forecast_summary.csv (model metrics)
- reports/model_evaluation_report.md
- reports/forecast_vs_actual.png
- notebooks/week3_prophet_evaluation.ipynb

✅ **Metrics:**
- MAE: 4,096.57 units
- RMSE: 5,337.33 units
- MAPE: 680.16%

---

### COMMIT 4: Results Consolidation (Day 4)
✅ **Responsibilities:**
- Created actual vs predicted comparison
- Consolidated all forecast outputs
- Prepared data for Power BI dashboard

✅ **Deliverables:**
- data/processed/actual_vs_predicted.csv (574 rows - with error analysis)

---

## Data Summary

| Dataset | Rows | Columns | Date Range |
|---------|------|---------|------------|
| train_data.csv | 1,339 | 31 | 2011-01-29 to 2014-09-28 |
| test_data.csv | 574 | 31 | 2014-09-29 to 2016-04-24 |
| forecast_output.csv | 574 | 4 | 2014-09-29 to 2016-04-24 |
| forecast_results.csv | 574 | 6 | 2014-09-29 to 2016-04-24 |
| actual_vs_predicted.csv | 574 | 5 | 2014-09-29 to 2016-04-24 |

---

## Model Performance

**Prophet Configuration:**
- Yearly seasonality: ✅ Enabled
- Weekly seasonality: ✅ Enabled
- Daily seasonality: ✅ Enabled
- Confidence interval: 95%

**Evaluation Metrics:**
- MAE: 4,096.57 units (average daily error)
- RMSE: 5,337.33 units (penalizes larger errors)
- MAPE: 680.16% (high due to daily anomalies)

**Key Findings:**
✅ Model captures overall sales trend (30,000-40,000 units/day)
✅ Provides good confidence intervals (95% CI)
✅ Smooth trend decomposition
❌ Struggles with daily volatility
❌ Cannot predict sudden drops (anomalies)
✅ Better for weekly/monthly forecasting

---

## Files Available

### Data Files (data/processed/)
- train_data.csv
- test_data.csv
- forecast_output.csv
- forecast_results.csv
- forecast_summary.csv
- actual_vs_predicted.csv

### Report Files (reports/)
- data_validation_report.md
- feature_reference.md
- model_evaluation_report.md
- forecast_vs_actual.png

### Notebook Files (notebooks/)
- week3_prophet_colab.ipynb
- week3_prophet_evaluation.ipynb

---

## For Week 4 Teams

### Power BI Dashboard Team
Use files:
- forecast_results.csv - for trend visualization
- forecast_summary.csv - for metrics reporting
- forecast_vs_actual.png - as reference

Create:
- Forecast vs actual comparison charts
- Confidence interval bands
- Weekly/monthly aggregated views
- Model performance metrics display

### Streamlit Deployment Team
Use files:
- forecast_results.csv - for interactive forecasts
- actual_vs_predicted.csv - for error analysis
- model_evaluation_report.md - for documentation

Features:
- Date range filtering
- Forecast values with confidence intervals
- Actual vs predicted comparison
- Model metrics display

---

## Recommendations for Production

✅ **Immediate (Use as-is):**
- Weekly/monthly aggregated forecasts
- Trend analysis and planning
- Dashboard visualizations
- Confidence interval display

⚠️ **Short-term improvements:**
- Handle anomalies separately
- Aggregate to weekly/monthly before using
- Apply to categories without anomalies

🔧 **Medium-term enhancements:**
- Ensemble with LightGBM model
- Category-level Prophet models
- Feature engineering (promotions, holidays)
- Anomaly detection system

---

## Week 3 Status: COMPLETE ✅

All deliverables created and ready.
Next: Hand off to Week 4 Power BI & Streamlit teams.
