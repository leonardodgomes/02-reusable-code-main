-- ============================================================
-- MERGE / UPSERT TEMPLATE (SCD Type 1)
-- Purpose:
--   - Insert new records
--   - Update existing records in place (overwrite)
--   - No historical tracking (Type 1)
-- Use cases:
--   - Dimensions without history
--   - Reference tables
--   - Deduplicated fact loads
-- ============================================================

MERGE INTO target_table AS tgt
USING staging_table AS src
    -- Match records based on the business key or primary key
    ON tgt.primary_key = src.primary_key

WHEN MATCHED THEN
    -- When the record already exists, update it with the latest values
    UPDATE SET
        tgt.col1 = src.col1,
        tgt.col2 = src.col2,
        tgt.updated_at = CURRENT_TIMESTAMP

WHEN NOT MATCHED THEN
    -- When the record does not exist, insert it
    INSERT (
        primary_key,
        col1,
        col2,
        created_at
    )
    VALUES (
        src.primary_key,
        src.col1,
        src.col2,
        CURRENT_TIMESTAMP
    );
