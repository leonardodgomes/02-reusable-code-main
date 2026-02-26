-- =====================================================================
-- FILE: caching_and_materialization.sql
-- PURPOSE:
--   SQL patterns for improving performance using caching, materialized
--   views, and precomputed tables.
--
-- WHAT'S INCLUDED:
--   - Caching tables (Databricks)
--   - Materialized views
--   - Refresh strategies
--   - Pre-aggregation patterns
--
-- WHEN TO USE:
--   Use these patterns when queries are repeatedly executed or when
--   dashboards require fast response times.
-- =====================================================================


-- ============================
-- DATABRICKS CACHE TABLE
-- ============================

CACHE TABLE dim_customer;


-- ============================
-- MATERIALIZED VIEW
-- ============================

CREATE MATERIALIZED VIEW mv_daily_sales AS
SELECT
    sale_date,
    SUM(sale_amount) AS total_sales
FROM fact_sales
GROUP BY sale_date;
