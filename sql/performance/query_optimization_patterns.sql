-- =====================================================================
-- FILE: query_optimization_patterns.sql
-- PURPOSE:
--   SQL rewrite patterns that transform slow queries into fast ones.
--
-- WHAT'S INCLUDED:
--   - Rewriting subqueries
--   - Eliminating unnecessary DISTINCT
--   - Using EXISTS instead of IN
--   - Using JOINs instead of correlated subqueries
--   - Predicate pushdown
--
-- WHEN TO USE:
--   Use these patterns when queries are slow, scanning too much data,
--   or performing unnecessary work.
-- =====================================================================


-- ============================
-- BAD: IN SUBQUERY (slow)
-- ============================

SELECT *
FROM fact_sales
WHERE customer_id IN (
    SELECT customer_id FROM dim_customer WHERE is_active = TRUE
);


-- ============================
-- GOOD: EXISTS (fast)
-- ============================

SELECT fs.*
FROM fact_sales fs
WHERE EXISTS (
    SELECT 1
    FROM dim_customer dc
    WHERE dc.customer_id = fs.customer_id
      AND dc.is_active = TRUE
);


-- ============================
-- BAD: CORRELATED SUBQUERY
-- ============================

SELECT
    customer_id,
    (SELECT MAX(sale_amount)
     FROM fact_sales fs2
     WHERE fs2.customer_id = fs1.customer_id) AS max_sale
FROM fact_sales fs1;


-- ============================
-- GOOD: WINDOW FUNCTION
-- ============================

SELECT
    customer_id,
    MAX(sale_amount) OVER (PARTITION BY customer_id) AS max_sale
FROM fact_sales;
