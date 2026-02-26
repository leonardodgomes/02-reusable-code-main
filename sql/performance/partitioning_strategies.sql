-- =====================================================================
-- FILE: partitioning_strategies.sql
-- PURPOSE:
--   SQL patterns for table partitioning to improve performance on large
--   datasets, especially time-series or fact tables.
--
-- WHAT'S INCLUDED:
--   - Date-based partitioning
--   - Range partitioning
--   - Hash partitioning
--   - Partition pruning examples
--
-- WHEN TO USE:
--   Use partitioning when tables exceed millions of rows and queries
--   frequently filter by date or category.
--
-- NOTES:
--   Partitioning improves read performance but increases metadata cost.
-- =====================================================================


-- ============================
-- DATE-BASED PARTITIONING
-- ============================

CREATE TABLE fact_sales_partitioned (
    sale_id BIGINT,
    customer_id BIGINT,
    sale_amount DECIMAL(10,2),
    sale_date DATE
)
PARTITION BY (sale_date);


-- ============================
-- RANGE PARTITIONING
-- ============================

CREATE TABLE customer_age_partitioned (
    customer_id BIGINT,
    age INT
)
PARTITION BY RANGE (age) (
    PARTITION p1 VALUES LESS THAN (20),
    PARTITION p2 VALUES LESS THAN (40),
    PARTITION p3 VALUES LESS THAN (60),
    PARTITION p4 VALUES LESS THAN (80)
);


-- ============================
-- HASH PARTITIONING
-- ============================

CREATE TABLE orders_hash_partitioned (
    order_id BIGINT,
    customer_id BIGINT
)
PARTITION BY HASH (customer_id);
