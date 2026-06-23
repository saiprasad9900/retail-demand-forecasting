# Feature Reference Document
## Week 3 Prophet Modeling - Feature Definitions

### Overview
31 total columns: 3 identifiers + 1 target + 27 engineered features

---

## IDENTIFIERS (Not used in modeling)
1. **d** - Row index
2. **date** - Date column (YYYY-MM-DD)
3. **wm_yr_wk** - Walmart year-week identifier

## TARGET VARIABLE (What we predict)
- **total_sales** - Daily total sales in units

---

## ENGINEERED FEATURES (27 total)

### Time Features (6)
- **month** - Month of year (1-12)
- **year** - Year (2011-2016)
- **day_of_week** - Day of week (0=Monday, 6=Sunday)
- **is_weekend** - Binary flag (1=weekend, 0=weekday)
- **day_of_year** - Day number in year (1-365)
- **week_of_year** - Week number in year (1-53)

### Event Features (2)
- **event_name_1** - Name of event (NaN on non-event days)
- **event_type_1** - Type of event e.g., Cultural, Sporting (NaN on non-event days)

### Holiday Features (1)
- **is_holiday** - Binary flag for holiday (1=holiday, 0=normal)

### SNAP Features (5) - CRITICAL FOR FORECASTING
- **snap_CA** - SNAP day in California (1=yes, 0=no)
- **snap_TX** - SNAP day in Texas (1=yes, 0=no)
- **snap_WI** - SNAP day in Wisconsin (1=yes, 0=no)
- **snap_active** - Any state SNAP active (1=yes, 0=no)
- **is_snap_day** - SNAP day flag (1=yes, 0=no)
- **Note:** snap_active and is_snap_day are redundant (same meaning)
- **Impact:** +11% demand uplift on SNAP days (critical insight from Week 2)

### Lag Features (3) - Recent Sales History
- **sales_lag_7** - Sales from 7 days ago
- **sales_lag_14** - Sales from 14 days ago
- **sales_lag_28** - Sales from 28 days ago
- **Note:** NaN for first 28 days (no prior data)

### Rolling Average Features (3) - Trend Smoothing
- **rolling_mean_7** - 7-day moving average (weekly trend)
- **rolling_mean_14** - 14-day moving average (2-week trend)
- **rolling_mean_30** - 30-day moving average (monthly trend)
- **Purpose:** Smooth daily noise to reveal underlying trends

### Cyclical Features (4) - Seasonality Encoding
- **month_sin** - Sine encoding of month (circular)
- **month_cos** - Cosine encoding of month (circular)
- **day_sin** - Sine encoding of day (circular)
- **day_cos** - Cosine encoding of day (circular)
- **Purpose:** Encode seasonal patterns (Dec-Jan are neighbors, not far apart)

### Price Features (3)
- **avg_price** - Average daily price ($)
- **price_lag_7** - Average price from 7 days ago
- **price_change** - Daily percentage change in price (%)
- **Note:** Price is stable (0.0051% daily change on average)

---

## Missing Values (Expected)
- **event_name_1, event_type_1**: NaN on non-event days (about 95% missing)
- **sales_lag_7/14/28**: NaN for first 7/14/28 days respectively
- **All other features**: 0 missing values

---

## Data Quality Summary
✅ 1913 daily observations
✅ Complete date continuity (no gaps)
✅ All features properly engineered
✅ Ready for Prophet modeling
