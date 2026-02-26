-- =====================================================================
-- FILE: indexing_strategies.sql
-- PURPOSE:
--   This file contains best-practice indexing patterns to improve query
--   performance, reduce table scans, and optimize joins and filters.
--
-- WHAT'S INCLUDED:
--   - Single-column indexes
--   - Composite indexes
--   - Covering indexes
--   - Indexes for JOIN performance
--   - Indexes for filtering and sorting
--
-- WHEN TO USE:
--   Use these patterns when queries are slow due to full table scans,
--   heavy filtering, or expensive joins.
--
-- NOTES:
--   Indexing strategy depends on workload. Over-indexing harms writes.
-- =====================================================================


-- ============================
-- SINGLE-COLUMN INDEX
-- ============================

CREATE INDEX idx_customer_email
ON dim_customer (email);


-- ============================
-- COMPOSITE INDEX
-- (Useful when filtering by multiple columns)
-- ============================

CREATE INDEX idx_sales_customer_date
ON fact_sales (customer_id, sale_date);


-- ============================
-- COVERING INDEX
-- (Index includes all columns needed for the query)
-- ============================

CREATE INDEX idx_sales_covering
ON fact_sales (customer_id, sale_date, sale_amount);


-- ============================
-- INDEX FOR JOIN PERFORMANCE
-- ============================

CREATE INDEX idx_dim_customer_sk
ON dim_customer (customer_sk);
