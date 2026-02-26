-- ============================================================
-- DATA CLEANSING TEMPLATE
-- Purpose:
--   - Standardize text fields
--   - Normalize phone numbers
--   - Clean whitespace and casing
-- Use cases:
--   - Customer data
--   - CRM ingestion
--   - Data quality pipelines
-- ============================================================

UPDATE customer
SET
    email = LOWER(TRIM(email)),                 -- Normalize email
    phone = REGEXP_REPLACE(phone, '[^0-9]', ''), -- Keep only digits
    name = INITCAP(name)                        -- Capitalize names
WHERE 1 = 1;
