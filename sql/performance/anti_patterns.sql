-- =====================================================================
-- FILE: anti_patterns.sql
-- PURPOSE:
--   Common SQL anti-patterns that cause performance issues, with
--   explanations and corrected versions.
--
-- WHAT'S INCLUDED:
--   - SELECT *
--   - Functions on indexed columns
--   - OR conditions preventing index use
--   - Non-SARGable predicates
--   - Unnecessary DISTINCT
--
-- WHEN TO USE:
--   Use this file to review and avoid slow SQL patterns.
-- =====================================================================


-- ============================
-- ANTI-PATTERN: SELECT *
-- ============================

-- BAD:
SELECT * FROM fact_sales;

-- GOOD:
SELECT sale_id, customer_id, sale_amount FROM fact_sales;


-- ============================
-- ANTI-PATTERN: FUNCTION ON INDEXED COLUMN
-- ============================

-- BAD:
SELECT * FROM dim_customer WHERE LOWER(email) = 'test@test.com';

-- GOOD:
SELECT * FROM dim_customer WHERE email = LOWER('test@test.com');


-- ============================
-- ANTI-PATTERN: OR CONDITIONS
-- ============================

-- BAD:
SELECT * FROM sales WHERE region = 'EU' OR region = 'US';

-- GOOD:
SELECT * FROM sales WHERE region IN ('EU', 'US');
