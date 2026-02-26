-- =====================================================================
-- FILE: market_basket_analysis.sql
-- PURPOSE:
--   SQL templates for association rule mining and product affinity
--   analysis (market basket analysis).
-- =====================================================================


-- ============================
-- PRODUCT CO-OCCURRENCE MATRIX
-- ============================

SELECT
    a.product_id AS product_a,
    b.product_id AS product_b,
    COUNT(*) AS co_occurrence
FROM silver.order_items a
JOIN silver.order_items b
    ON a.order_id = b.order_id
   AND a.product_id <> b.product_id
GROUP BY product_a, product_b;


-- ============================
-- SUPPORT, CONFIDENCE, LIFT
-- ============================

WITH item_counts AS (
    SELECT product_id, COUNT(*) AS cnt
    FROM silver.order_items
    GROUP BY product_id
),
pair_counts AS (
    SELECT
        a.product_id AS a,
        b.product_id AS b,
        COUNT(*) AS pair_cnt
    FROM silver.order_items a
    JOIN silver.order_items b
        ON a.order_id = b.order_id
       AND a.product_id <> b.product_id
    GROUP BY a, b
)
SELECT
    p.a,
    p.b,
    p.pair_cnt AS support_ab,
    p.pair_cnt * 1.0 / i1.cnt AS confidence_a_to_b,
    (p.pair_cnt * 1.0 / i1.cnt) /
        (i2.cnt * 1.0 / (SELECT COUNT(*) FROM silver.order_items)) AS lift
FROM pair_counts p
JOIN item_counts i1 ON p.a = i1.product_id
JOIN item_counts i2 ON p.b = i2.product_id;
