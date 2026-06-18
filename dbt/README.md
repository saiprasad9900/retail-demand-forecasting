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