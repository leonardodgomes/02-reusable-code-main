-- =====================================================================
-- FILE: advanced_time_series.sql
-- PURPOSE:
--   Advanced SQL patterns for time-series analytics, including YTD/MTD,
--   rolling windows, seasonality, and period-based comparisons.
--
-- WHAT'S INCLUDED:
--   - YTD, MTD, WTD calculations
--   - Rolling windows (ROWS and RANGE)
--   - Seasonality detection
--   - Time bucketing (hour, week, fiscal)
--   - YoY and MoM comparisons
--
-- WHEN TO USE:
--   For dashboards, forecasting inputs, and trend analysis.
-- =====================================================================


-- ============================
-- YEAR-TO-DATE (YTD)
-- ============================

SELECT
    sale_date,
    sale_amount,
    SUM(sale_amount) OVER (
        PARTITION BY YEAR(sale_date)
        ORDER BY sale_date
    ) AS ytd_sales
FROM silver.sales_daily;


-- ============================
-- MONTH-TO-DATE (MTD)
-- ============================

SELECT
    sale_date,
    sale_amount,
    SUM(sale_amount) OVER (
        PARTITION BY DATE_TRUNC('month', sale_date)
        ORDER BY sale_date
    ) AS mtd_sales
FROM silver.sales_daily;


-- ============================
-- WEEK-TO-DATE (WTD)
-- ============================

SELECT
    sale_date,
    sale_amount,
    SUM(sale_amount) OVER (
        PARTITION BY DATE_TRUNC('week', sale_date)
        ORDER BY sale_date
    ) AS wtd_sales
FROM silver.sales_daily;


-- ============================
-- YEAR-OVER-YEAR (YoY)
-- ============================

WITH yearly AS (
    SELECT
        YEAR(sale_date) AS year,
        SUM(sale_amount) AS total_sales
    FROM silver.sales_daily
    GROUP BY YEAR(sale_date)
)
SELECT
    year,
    total_sales,
    LAG(total_sales) OVER (ORDER BY year) AS prev_year_sales,
    total_sales - LAG(total_sales) OVER (ORDER BY year) AS yoy_delta,
    (total_sales / NULLIF(LAG(total_sales) OVER (ORDER BY year), 0) - 1) AS yoy_growth
FROM yearly;


-- ============================
-- SE