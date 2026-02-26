-- =====================================================================
-- FILE: geospatial_analytics.sql
-- PURPOSE:
--   SQL patterns for geospatial analytics: distance calculations,
--   clustering, and geographic aggregations.
-- =====================================================================


-- ============================
-- HAVERSINE DISTANCE (KM)
-- ============================

SELECT
    customer_id,
    6371 * ACOS(
        COS(RADIANS(lat1)) * COS(RADIANS(lat2)) *
        COS(RADIANS(lon2) - RADIANS(lon1)) +
        SIN(RADIANS(lat1)) * SIN(RADIANS(lat2))
    ) AS distance_km
FROM silver.customer_locations;
