-- ============================================================
-- SCD TYPE 2 TEMPLATE
-- Purpose:
--   - Maintain full history of changes
--   - Close old records when a change is detected
--   - Insert a new "current" version of the record
-- Use cases:
--   - Customer profiles
--   - Product attributes
--   - Employee records
-- ============================================================

MERGE INTO dim_customer AS tgt
USING staging_customer AS src
    -- Match only the CURRENT version of the record
    ON tgt.customer_id = src.customer_id
    AND tgt.is_current = TRUE

WHEN MATCHED AND (
        -- Detect changes in tracked attributes
        tgt.customer_name <> src.customer_name
        OR tgt.email <> src.email
    )
THEN
    -- Close the existing record (end-date it)
    UPDATE SET
        tgt.is_current = FALSE,
        tgt.valid_to = CURRENT_DATE

WHEN NOT MATCHED THEN
    -- Insert a new version of the record
    INSERT (
        customer_id,
        customer_name,
        email,
        valid_from,
        valid_to,
        is_current
    )
    VALUES (
        src.customer_id,
        src.customer_name,
        src.email,
        CURRENT_DATE,   -- Start of validity
        NULL,           -- Still active
        TRUE            -- Mark as current version
    );
