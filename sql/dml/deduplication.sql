-- ============================================================
-- DEDUPLICATION TEMPLATE
-- Purpose:
--   - Remove duplicate records based on a business key
--   - Keep the most recent version (based on updated_at)
-- Use cases:
--   - Raw ingestion layers
--   - CDC streams with duplicates
--   - Cleaning up poorly ingested data
-- ============================================================

WITH ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY business_key
            ORDER BY updated_at DESC   -- Keep the newest record
        ) AS rn
    FROM raw_table
)

-- Select only the first (best) record per business key
SELECT *
FROM ranked
WHERE rn = 1;
