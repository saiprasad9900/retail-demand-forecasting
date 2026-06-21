# dbt models

This folder contains simple dbt models that aggregate a raw daily sales table into weekly and monthly summaries.

How to use

- Configure your `profiles.yml` for your data warehouse and ensure a `raw.daily_sales` source is defined.
- Run the models:

```bash
dbt run --models weekly_sales monthly_sales
dbt test --models weekly_sales monthly_sales
```

Fields created
- `week_start` / `month_start`: period start date
- `total_sales`: SUM of `sales_amount`
- `total_quantity`: SUM of `quantity`
- `transaction_count`: COUNT DISTINCT `transaction_id`
Here’s a simple explanation of that table:

month_start: The month (period) start date — the aggregate covers that whole month.
total_sales: Sum of daily sales for that month (currency/units as in your source).
day_count: Number of daily records included in the sum for that month.
Interpretation examples:

Row 2011-01-01, 88163, 3 → the dataset has 3 days in January 2011 and their sales sum to 88,163 (average ≈ 29,387.67 per day).
Row 2011-02-01, 726375, 28 → February 2011 has 28 days in the data with total sales 726,375 (average ≈ 25,941.96/day).
Row 2011-03-01, 763567, 31 → March 2011 has 31 days and total sales 763,567 (average ≈ 24,631.52/day).
Note: a small day_count (like 3 for Jan 2011) means the month is only partially present in the source data — check for missing days if you expect full-month coverage.
Week Analysis

File: weekly_sales.csv
week_start: Start date of the week used for aggregation (the period’s first day).
total_sales: Sum of daily sales for that week.
day_count: Number of daily records included in the week’s sum.
Examples and interpretation:

Row 2011-01-24, 64380, 2 → only 2 days from that week are present, summing to 64,380 (avg ≈ 32,190/day).
Row 2011-01-31, 196230, 7 → full week with 7 days, total sales 196,230 (avg ≈ 28,033/day).
Notes and next steps:

Partial weeks: Small day_count means the week is incomplete in the source — verify missing days if you expect full weeks.
Average daily sales: Useful to add as avg_daily = total_sales / day_count.

# dbt Transformations

## Overview

This folder contains the dbt models developed during Week 2 of the Retail Demand Forecasting project.

The objective of these models is to transform daily sales data into weekly and monthly aggregated views that can be used for analysis and support future demand forecasting tasks.

---

## Aggregation Models

### weekly_sales.sql

This model aggregates daily sales records into weekly summaries.

**Output:**

* weekly_sales.csv

### monthly_sales.sql

This model aggregates daily sales records into monthly summaries.

**Output:**

* monthly_sales.csv

---

## Data Marts

The following analytical marts were created from the cleaned sales dataset during Week 2.

### Store Mart

**Output:**

* store_mart.csv

**Purpose:**

* Store-level sales analysis
* Store performance comparison

### State Mart

**Output:**

* state_mart.csv

**Purpose:**

* Regional sales analysis
* State-level performance comparison

### Product Mart

**Output:**

* product_mart.csv

**Purpose:**

* Product-level sales analysis
* Identification of high-demand products

---

## Data Lineage

Raw M5 Dataset

→ Data Cleaning

→ Feature Engineering

→ Weekly Aggregation (dbt)

→ Monthly Aggregation (dbt)

→ Store Mart / State Mart / Product Mart

→ Forecasting Models (Week 3)

---

## Outputs Generated

* weekly_sales.csv
* monthly_sales.csv
* store_mart.csv
* state_mart.csv
* product_mart.csv

---

## Note on Tooling

The original project specification recommended using Google BigQuery or Snowflake as the data warehouse layer. For this implementation, processed CSV datasets were used as the primary source for transformations and analysis.
