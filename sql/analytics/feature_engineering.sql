-- =====================================================================
-- FILE: feature_engineering.sql
-- PURPOSE:
--   SQL patterns for ML feature engineering: lag features, rolling stats,
--   frequency encoding, and time-based features.
-- =====================================================================


-- ============================
-- LAG FEATURES
-- ============================

SELECT
    sale_date,
    sale_amount,
    LAG(sale_amount, 1) OVER (ORDER BY sale_date) AS prev_day_sales
FROM silver.sales_daily;


-- ============================
-- ROLLING VOLATILITY
-- ============================

SELECT
    sale_date,
    sale_amount,
    STDDEV(sale_amount) OVER (
        ORDER BY sale_date
        ROWS BETWEEN 30 PRECEDING AND CURRENT ROW
    ) AS rolling_volatility_30d
FROM silver.sales_daily;
