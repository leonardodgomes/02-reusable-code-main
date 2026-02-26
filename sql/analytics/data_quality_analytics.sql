-- =====================================================================
-- FILE: data_quality_analytics.sql
-- PURPOSE:
--   SQL patterns for evaluating data quality: null rates, duplicates,
--   schema drift, and outlier detection.
-- =====================================================================


-- ============================
-- NULL RATE PER COLUMN
-- ============================

SELECT
    column_name,
    SUM(CASE WHEN value IS NULL THEN 1 END) AS null_count,
    COUNT(*) AS total_rows,
    SUM(CASE WHEN value IS NULL THEN 1 END) * 1.0 / COUNT(*) AS null_rate
FROM silver.table
UNPIVOT (value FOR column_name IN (*));
