-- =====================================================================
-- FILE: customer_analytics_advanced.sql
-- PURPOSE:
--   Advanced SQL patterns for customer analytics: retention, churn,
--   lifetime value, funnels, and behavioral segmentation.
-- =====================================================================


-- ============================
-- COHORT RETENTION ANALYSIS
-- ============================

WITH cohort AS (
    SELECT
        customer_id,
        MIN(DATE_TRUNC('month', sale_date)) AS cohort_month
    FROM silver.sales
    GROUP BY customer_id
),
activity AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', sale_date) AS activity_month
    FROM silver.sales
)
SELECT
    cohort.cohort_month,
    activity.activity_month,
    COUNT(DISTINCT activity.customer_id) AS active_customers
FROM cohort
JOIN activity USING (customer_id)
GROUP BY cohort.cohort_month, activity.activity_month
ORDER BY cohort.cohort_month, activity.activity_month;


-- ============================
-- CHURN DETECTION
-- ============================

SELECT
    customer_id,
    MAX(sale_date) AS last_purchase,
    CASE WHEN MAX(sale_date) < CURRENT_DATE - INTERVAL '90' DAY
         THEN TRUE ELSE FALSE END AS is_churned
FROM silver.sales
GROUP BY customer_id;


-- ============================
-- CUSTOMER LIFETIME VALUE (CLV)
-- ============================

SELECT
    customer_id,
    COUNT(*) AS total_orders,
    AVG(sale_amount) AS avg_order_value,
    SUM(sale_amount) AS lifetime_value,
    MAX(sale_date) AS last_purchase,
    CURRENT_DATE - MAX(sale_date) AS days_since_last_purchase
FROM silver.sales
GROUP BY customer_id;
