-- =====================================================================
-- FILE: execution_plan_analysis.sql
-- PURPOSE:
--   SQL patterns for inspecting and interpreting execution plans to
--   diagnose performance issues.
--
-- WHAT'S INCLUDED:
--   - EXPLAIN plans
--   - Identifying table scans
--   - Detecting missing indexes
--   - Join strategy analysis
--
-- WHEN TO USE:
--   Use this file when queries are slow and you need to understand why.
-- =====================================================================


-- ============================
-- BASIC EXPLAIN PLAN
-- ============================

EXPLAIN SELECT * FROM fact_sales WHERE sale_amount > 100;


-- ============================
-- EXPLAIN WITH FORMATTING
-- ============================

EXPLAIN FORMATTED
SELECT fs.*, dc.customer_name
FROM fact_sales fs
JOIN dim_customer dc
    ON fs.customer_id = dc.customer_id;
