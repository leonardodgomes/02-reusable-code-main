-- =====================================================================
-- FILE: anomaly_detection.sql
-- PURPOSE:
--   SQL templates for detecting anomalies and outliers using statistical
--   and rule-based methods.
--
-- WHAT'S INCLUDED:
--   - Z-score detection
--   - Rolling median + MAD
--   - Threshold-based anomalies
--   - Volume spikes/drops
-- =====================================================================


-- ============================
-- Z-SCORE ANOMALY DETECTION
-- ============================

WITH stats AS (
    SELECT
        sale_date,
        sale_amount,
        AVG(sale_amount) OVER () AS mean_sales,
        STDDEV(sale_amount) OVER () AS std_sales
    FROM silver.sales_daily
)
SELECT
    *,
    (sale_amount - mean_sales) / std_sales AS z_score,
    CASE WHEN ABS((sale_amount - mean_sales) / std_sales) > 3
         THEN TRUE ELSE FALSE END AS is_anomaly
FROM stats;


-- ============================
-- ROLLING MEDIAN + MAD
-- ============================

WITH rolling AS (
    SELECT
        sale_date,
        sale_amount,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY sale_amount)
            OVER (ORDER BY sale_date ROWS BETWEEN 7 PRECEDING AND CURRENT ROW) AS rolling_median,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY ABS(sale_amount -
            PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY sale_amount)
                OVER (ORDER BY sale_date ROWS BETWEEN 7 PRECEDING AND CURRENT ROW)))
            OVER (ORDER BY sale_date ROWS BETWEEN 7 PRECEDING AND CURRENT ROW) AS mad
    FROM silver.sales_daily
)
SELECT
    *,
    CASE WHEN ABS(sale_amount - rolling_median) > 3 * mad
         THEN TRUE ELSE FALSE END AS is_outlier
FROM rolling;
