-- =====================================================================
-- WINDOW FUNCTIONS TEMPLATE
-- Purpose:
--   - Provide reusable patterns for ranking, running totals,
--     moving averages, lag/lead comparisons, and partitioned analytics.
-- =====================================================================

-- ============================================================
-- ROW_NUMBER: Deduplication or picking latest record
-- ============================================================

SELECT
    *,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY updated_at DESC
    ) AS rn
FROM silver.customer_events;

-- ============================================================
-- RUNNING TOTAL (Cumulative sum)
-- ============================================================

SELECT
    sale_date,
    sale_amount,
    SUM(sale_amount) OVER (
        ORDER BY sale_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM silver.sales_daily;

-- ============================================================
-- MOVING AVERAGE (7-day rolling)
-- ============================================================

SELECT
    sale_date,
    sale_amount,
    AVG(sale_amount) OVER (
        ORDER BY sale_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS moving_avg_7d
FROM silver.sales_daily;

-- ============================================================
-- LAG / LEAD (Period-over-period comparison)
-- ============================================================

SELECT
    sale_date,
    sale_amount,
    LAG(sale_amount, 1) OVER (ORDER BY sale_date) AS prev_day_sales,
    sale_amount - LAG(sale_amount, 1) OVER (ORDER BY sale_date) AS delta_sales
FROM silver.sales_daily;


