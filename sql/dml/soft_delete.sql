-- ============================================================
-- SOFT DELETE TEMPLATE
-- Purpose:
--   - Mark records as deleted instead of physically removing them
--   - Maintain auditability and historical tracking
-- Use cases:
--   - GDPR compliance
--   - Logical deletes in dimensions
--   - Systems that require reversible deletes
-- ============================================================

UPDATE target_table tgt
SET
    is_deleted = TRUE,
    deleted_at = CURRENT_TIMESTAMP
WHERE tgt.primary_key NOT IN (
    -- Records that still exist in the source
    SELECT primary_key FROM staging_table
);
