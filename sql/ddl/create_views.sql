-- ============================================================
-- GENERIC VIEW TEMPLATE
-- Purpose:
--   - Abstract complex logic
--   - Provide a clean interface for BI tools
--   - Avoid duplicating logic across queries
-- ============================================================

CREATE OR REPLACE VIEW vw_customer_clean AS
SELECT
    customer_id,
    INITCAP(customer_name) AS customer_name,
    LOWER(email) AS email,
    REGEXP_REPLACE(phone, '[^0-9]', '') AS phone_clean,
    created_at
FROM dim_customer
WHERE is_active = TRUE;

-- ============================================================
-- AGGREGATION VIEW TEMPLATE
-- Purpose:
--   - Pre-aggregate data for performance
--   - Reduce load on BI dashboards
-- ============================================================

CREATE OR REPLACE VIEW vw_sales_daily AS
SELECT
    sale_date,
    SUM(sale_amount) AS total_sales,
    SUM(quantity) AS total_units
FROM fact_sales
GROUP BY sale_date;
