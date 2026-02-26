-- =====================================================================
-- SCHEMA CREATION TEMPLATE (ADVANCED)
-- Purpose:
--   - Provide a standardized way to organize database objects
--   - Improve governance, security, and separation of responsibilities
--   - Support multi-layer data architecture (raw → curated → analytics)
--   - Ensure consistent naming conventions across environments
-- =====================================================================

-- =====================================================================
-- SECTION 1: ENVIRONMENT-LEVEL SCHEMAS
-- These schemas represent the typical layers of a modern data platform.
-- They help separate ingestion, transformation, and consumption workloads.
-- =====================================================================

-- RAW / LANDING LAYER
-- - Stores unprocessed data exactly as received
-- - Minimal transformations
-- - Often used for audit and replay
CREATE SCHEMA IF NOT EXISTS raw;

-- BRONZE / REFINED LAYER
-- - Lightly cleaned and standardized data
-- - Basic type casting, deduplication, and normalization
CREATE SCHEMA IF NOT EXISTS bronze;

-- SILVER / CURATED LAYER
-- - Business-ready tables
-- - Conformed dimensions, enriched facts
-- - Used by analysts and downstream systems
CREATE SCHEMA IF NOT EXISTS silver;

-- GOLD / ANALYTICS LAYER
-- - Aggregated, optimized tables for BI dashboards
-- - Pre-calculated metrics, KPIs, and semantic models
CREATE SCHEMA IF NOT EXISTS gold;

-- SANDBOX / EXPERIMENTAL LAYER
-- - Safe space for analysts or data scientists
-- - Allows experimentation without affecting production
CREATE SCHEMA IF NOT EXISTS sandbox;

-- =====================================================================
-- SECTION 2: DOMAIN-DRIVEN SCHEMAS
-- These schemas follow a Data Mesh or Domain-Driven Design approach.
-- Useful when teams own their own data products.
-- =====================================================================

CREATE SCHEMA IF NOT EXISTS sales;
CREATE SCHEMA IF NOT EXISTS marketing;
CREATE SCHEMA IF NOT EXISTS finance;
CREATE SCHEMA IF NOT EXISTS hr;
CREATE SCHEMA IF NOT EXISTS operations;

-- =====================================================================
-- SECTION 3: COMMENTING SC