-- ============================================================
-- PRIMARY KEY & UNIQUE CONSTRAINTS
-- ============================================================

ALTER TABLE dim_customer
ADD CONSTRAINT pk_dim_customer PRIMARY KEY (customer_sk);

ALTER TABLE dim_customer
ADD CONSTRAINT uq_dim_customer_id UNIQUE (customer_id);

-- ============================================================
-- FOREIGN KEYS
-- ============================================================

ALTER TABLE fact_sales
ADD CONSTRAINT fk_sales_customer
FOREIGN KEY (customer_sk)
REFERENCES dim_customer(customer_sk);

-- ============================================================
-- INDEXES FOR PERFORMANCE
-- Purpose:
--   - Speed up joins and filters
--   - Improve query performance on large datasets
-- ============================================================

CREATE INDEX idx_sales_date
ON fact_sales (sale_date);

CREATE INDEX idx_customer_email
ON dim_customer (email);
