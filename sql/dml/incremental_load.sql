-- ============================================================
-- INCREMENTAL LOAD TEMPLATE
-- Purpose:
--   - Insert only new or changed records
--   - Avoid full reloads
--   - Compare timestamps to detect changes
-- Use cases:
--   - Fact tables
--   - CDC-based ingestion
--   - Daily incremental ETL
-- ============================================================

INSERT INTO fact_sales (
    sale_id,
    customer_id,
    amount,
    sale_date
)
SELECT
    src.sale_id,
    src.customer_id,
    src.amount,
    src.sale_date
FROM staging_sales src
LEFT JOIN fact_sales tgt
    ON src.sale_id = tgt.sale_id
WHERE
    -- New record
    tgt.sale_id IS NULL
    OR
    -- Changed record (based on timestamp)
    src.updated_at > tgt.updated_at;
