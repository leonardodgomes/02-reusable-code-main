-- =====================================================================
-- FILE: business_metrics_advanced.sql
-- PURPOSE:
--   SQL templates for advanced business metrics: profitability,
--   inventory turnover, funnels, and operational KPIs.
-- =====================================================================


-- ============================
-- INVENTORY TURNOVER
-- ============================

SELECT
    product_id,
    SUM(cost_of_goods_sold) / AVG(inventory_level) AS inventory_turnover
FROM silver.inventory
GROUP BY product_id;
