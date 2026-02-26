-- =====================================================================
-- FILE: text_analytics.sql
-- PURPOSE:
--   SQL patterns for keyword extraction, tokenization, sentiment scoring,
--   and text normalization.
-- =====================================================================


-- ============================
-- KEYWORD FREQUENCY
-- ============================

SELECT
    review_id,
    REGEXP_COUNT(LOWER(review_text), 'refund') AS refund_mentions
FROM silver.reviews;


-- ============================
-- SIMPLE SENTIMENT SCORING
-- ============================

SELECT
    review_id,
    review_text,
    CASE
        WHEN LOWER(review_text) LIKE '%good%' THEN 1
        WHEN LOWER(review_text) LIKE '%bad%' THEN -1
        ELSE 0
    END AS sentiment_score
FROM silver.reviews;
