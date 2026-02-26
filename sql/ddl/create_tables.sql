-- ============================================================
-- GENERIC TABLE CREATION TEMPLATE
-- Purpose:
--   - Provide a reusable structure for creating tables
--   - Includes metadata columns for auditing
--   - Supports identity keys and default timestamps
-- ============================================================

CREATE TABLE IF NOT EXISTS dim_customer (
    -- Surrogate key (recommended for dimensions)
    customer_sk BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    -- Natural/business key
    customer_id BIGINT NOT NULL,

    -- Attributes
    customer_name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(50),

    -- Audit columns
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- ============================================================
-- FACT TABLE TEMPLATE
-- Purpose:
--   - Store transactional data
--   - Use surrogate keys for joins
--   - Partitioning recommended for large tables
-- ============================================================

CREATE TABLE IF NOT EXISTS fact_sales (
    sale_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_sk BIGINT NOT NULL,
    product_sk BIGINT NOT NULL,
    quantity INT NOT NULL,
    sale_amount DECIMAL(10,2) NOT NULL,
    sale_date DATE NOT NULL,

    -- Audit columns
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
