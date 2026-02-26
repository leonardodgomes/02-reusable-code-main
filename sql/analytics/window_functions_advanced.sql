-- =====================================================================
-- ADVANCED WINDOW FUNCTIONS LIBRARY
-- Purpose:
--   - Provide a comprehensive set of reusable analytical SQL patterns
--   - Cover running totals, moving averages, ranking, segmentation,
--     time-series analytics, percent-of-total, and customer metrics
--   - Designed for Databricks, Snowflake, PostgreSQL, and other engines
-- =====================================================================


-- =====================================================================
-- SECTION 1 — RUNNING TOTALS
-- =====================================================================

-- Running total across all dates
SELECT
    sale_date,
    sale_amount,
    SUM(sale_amount) OVER (
        ORDER BY sale_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM silver.sales_daily;

-- Running total per customer
SELECT
    customer_id,
    sale_date,
    sale_amount,
    SUM(sale_amount) OVER (
        PARTITION BY customer_id
        ORDER BY sale_date
    ) AS running_total_customer
FROM silver.sales;


-- =====================================================================
-- SECTION 2 — MOVING AVERAGES
-- =====================================================================

-- 7-day moving average
SELECT
    sale_date,
    sale_amount,
    AVG(sale_amount) OVER (
        ORDER BY sale_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS moving_avg_7d
FROM silver.sales_daily;

-- 30-day moving average (time-based window)
SELECT
    sale_date,
    sale_amount,
    AVG(sale_amount) OVER (
        ORDER BY sale_date
        RANGE BETWEEN INTERVAL '30' DAY PRECEDING AND CURRENT ROW
    ) AS moving_avg_30d
FROM silver.sales_daily;


-- =====================================================================
-- SECTION 3 — PERIOD-OVER-PERIOD COMPARISONS
-- =====================================================================

-- Day-over-day comparison
SELECT
    sale_date,
    sale_amount,
    LAG(sale_amount, 1) OVER (ORDER BY sale_date) AS prev_day_sales,
    sale_amount - LAG(sale_amount, 1) OVER (ORDER BY sale_date) AS delta_sales
FROM silver.sales_daily;

-- Month-over-month growth
WITH monthly AS (
    SELECT
        DATE_TRUNC('month', sale_date) AS month,
        SUM(sale_amount) AS total_sales
    FROM silver.sales_daily
    GROUP BY DATE_TRUNC('month', sale_date)
)
SELECT
    month,
    total_sales,
    LAG(total_sales) OVER (ORDER BY month) AS prev_month_sales,
    (total_sales - LAG(total_sales) OVER (ORDER BY month)) AS delta,
    (total_sales / NULLIF(LAG(total_sales) OVER (ORDER BY month), 0) - 1) AS growth_rate
FROM monthly;


-- =====================================================================
-- SECTION 4 — PERCENT OF TOTAL
-- =====================================================================

SELECT
    product_id,
    SUM(sale_amount) AS product_sales,
    SUM(sale_amount) OVER () AS total_sales,
    SUM(sale_amount) * 1.0 / SUM(sale_amount) OVER () AS pct_of_total
FROM silver.sales
GROUP BY product_id;


-- =====================================================================
-- SECTION 5 — RANKING & TOP-N ANALYSIS
-- =====================================================================

-- Rank customers by revenue
SELECT
    customer_id,
    SUM(sale_amount) AS total_revenue,
    RANK() OVER (ORDER BY SUM(sale_amount) DESC) AS revenue_rank
FROM silver.sales
GROUP BY customer_id;

-- Top 3 products per category
SELECT *
FROM (
    SELECT
        category,
        product_id,
        SUM(sale_amount) AS total_sales,
        RANK() OVER (
            PARTITION BY category
            ORDER BY SUM(sale_amount) DESC
        ) AS rank_in_category
    FROM silver.sales
    GROUP BY category, product_id
) ranked
WHERE rank_in_category <= 3;


-- =====================================================================
-- SECTION 6 — SEGMENTATION & PERCENTILES
-- =====================================================================

-- Customer deciles
SELECT
    customer_id,
    total_revenue,
    NTILE(10) OVER (ORDER BY total_revenue DESC) AS revenue_decile
FROM silver.customer_revenue;

-- RFM scoring
SELECT
    customer_id,
    recency,
    frequency,
    monetary,
    NTILE(5) OVER (ORDER BY recency ASC) AS r_score,
    NTILE(5) OVER (ORDER BY frequency DESC) AS f_score,
    NTILE(5) OVER (ORDER BY monetary DESC) AS m_score
FROM silver.customer_rfm;


-- =====================================================================
-- SECTION 7 — TIME-SERIES ANALYTICS
-- =====================================================================

-- Week-to-date (WTD) and Month-to-date (MTD)
SELECT
    sale_date,
    sale_amount,
    SUM(sale_amount) OVER (
        PARTITION BY DATE_TRUNC('week', sale_date)
        ORDER BY sale_date
    ) AS wtd_sales,
    SUM(sale_amount) OVER (
        PARTITION BY DATE_TRUNC('month', sale_date)
        ORDER BY sale_date
    ) AS mtd_sales
FROM silver.sales_daily;

-- Seasonality: weekday averages
SELECT
    EXTRACT(DOW FROM sale_date) AS weekday,
    AVG(sale_amount) AS avg_sales
FROM silver.sales_daily
GROUP BY EXTRACT(DOW FROM sale_date);


-- =====================================================================
-- SECTION 8 — CUSTOMER ANALYTICS
-- =====================================================================

-- Customer lifetime value (simple model)
SELECT
    customer_id,
    SUM(sale_amount) AS lifetime_value
FROM silver.sales
GROUP BY customer_id;

-- Churn detection (no activity in last 90 days)
SELECT
    customer_id,
    MAX(sale_date) AS last_purchase_date,
    CASE
        WHEN MAX(sale_date) < CURRENT_DATE - INTERVAL '90' DAY
        THEN TRUE
        ELSE FALSE
    END AS is_churned
FROM silver.sales
GROUP BY customer_id;

-- Cohort analysis (retention)
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
