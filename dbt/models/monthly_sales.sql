-- Aggregates daily sales into monthly metrics
with daily as (
  select
    cast(sale_date as date) as sale_date,
    sales_amount,
    quantity,
    transaction_id
  from {{ source('raw', 'daily_sales') }}
)

select
  date_trunc('month', sale_date) as month_start,
  sum(sales_amount) as total_sales,
  sum(quantity) as total_quantity,
  count(distinct transaction_id) as transaction_count
from daily
group by 1
order by 1
