-- =====================================================================
-- FILE: distribution_analysis.sql
-- PURPOSE:
--   SQL patterns for analyzing distributions: percentiles, quartiles,
--   histograms, and boxplot metrics.
-- =====================================================================


-- ============================
-- QUARTILES & IQR
-- ============================

SELECT
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY sale_amount) AS q1,
    PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY sale_amount) AS median,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY sale_amount) AS q3,
    (PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY sale_amount) -
     PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY sale_amount)) AS iqr
FROM silver.sales;


-- ============================
-- HISTOGRAM BUCKETS
-- ============================

SELECT
    WIDTH_BUCKET(sale_amount, 0, 1000, 10) AS bucket,
    COUNT(*) AS count_in_bucket
FROM silver.sales
GROUP BY bucket
ORDER BY bucket;
