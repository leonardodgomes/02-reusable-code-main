-- ============================================================
-- SAFE DROP TEMPLATE
-- Purpose:
--   - Remove objects only if they exist
--   - Avoid errors during deployment
-- ============================================================

DROP VIEW IF EXISTS vw_customer_clean;
DROP VIEW IF EXISTS vw_sales_daily;

DROP TABLE IF EXISTS fact_sales;
DROP TABLE IF EXISTS dim_customer;

DROP SCHEMA IF EXISTS analytics CASCADE;
DROP SCHEMA IF EXISTS curated CASCADE;
DROP SCHEMA IF EXISTS refined CASCADE;
DROP SCHEMA IF EXISTS raw CASCADE;
