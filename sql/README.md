# 📚 SQL Project Library

**A Complete, Structured, Reusable SQL Toolkit**

This repository provides a fully organized SQL library covering **DDL, DML, Analytics, and Performance** patterns.

It is designed to support data engineering, analytics engineering, BI development, and advanced SQL learning.

Each folder contains:
- Clear file‑level descriptions
- Real‑world SQL templates
- Best practices
- Reusable patterns

## 📁 Folder Structure Overview

```
sql/
├── analytics/
├── ddl/
├── dml/
└── performance/
```


## 📊 1. analytics
Advanced analytical SQL patterns for BI, dashboards, data science, and feature engineering.

**Files included:**
- **advanced_time_series.sql**  
  Time‑series analytics: YTD, MTD, WTD, rolling windows, seasonality, YoY/MoM.

- **anomaly_detection.sql**  
Statistical and rule‑based anomaly detection: z‑score, MAD, thresholds.

- **business_metrics_advanced.sql**  
High‑value business KPIs: profitability, inventory turnover, funnels.

- **customer_analytics_advanced.sql**  
Customer behavior analytics: cohorts, churn, CLV, funnels.

- **data_quality_analytics.sql**  
Null rates, duplicates, schema drift, outlier detection.

- **distribution_analysis.sql**  
Percentiles, quartiles, histograms, IQR, distribution profiling.

- **feature_engineering.sql**  
Lag features, rolling stats, frequency encoding, target encoding.

- **geospatial_analytics.sql**  
Distance calculations, clustering, geographic aggregations.

- **market_basket_analysis.sql**  
Association rules: support, confidence, lift, co‑occurrence.

- **text_analytics.sql**  
Keyword extraction, regex tokenization, sentiment scoring.

- **window_functions_advanced.sql**  
Advanced window functions: ranking, moving averages, segmentation.

- **window_functions.sql**  
Core window function examples (introductory version).

## 🧱 2. ddl

Data Definition Language templates for building and managing database structures.

**Files included:**

- **constraints_and_indexes.sql**  
Primary keys, foreign keys, unique constraints, index creation.

- **create_schemas.sql**  
Schema creation, documentation, ownership, and permissions.

- **create_tables.sql**  
Table creation templates with best practices and comments.

- **create_views.sql**  
View creation patterns: standard views, materialized views.

- **drop_objects.sql**  
Safe drop patterns for tables, views, and schemas.

## 🔧 3. dml/
Data Manipulation Language patterns for ETL/ELT pipelines.

**Files included:**
- **data_cleansing.sql**  
Standardization, trimming, type casting, normalization.

- **deduplication.sql**  
Row‑level deduplication using ROW_NUMBER and grouping.

- **incremental_load.sql**  
Incremental ingestion patterns using timestamps or IDs.

- **merge_upsert.sql**  
Upsert logic using MERGE for slowly changing data.

- **scd_type_2.sql**  
Slowly Changing Dimension Type 2 implementation.

- **soft_delete.sql**  
Soft delete patterns using flags or end‑date logic.

## ⚡ 4. performance/
SQL performance optimization patterns for scalable workloads.

**Files included:**
- **anti_patterns.sql**  
Common mistakes that harm performance and how to fix them.

- **caching_and_materialization.sql**  
Caching, materialized views, pre‑aggregation strategies.

- **execution_plan_analysis.sql**  
How to inspect and interpret execution plans.

- **indexing_strategies.sql**  
Single, composite, covering, and join‑optimized indexes.

- **partitioning_strategies.sql**  
Date, range, and hash partitioning for large tables.

- **query_optimization_patterns.sql**  
Rewrite patterns (slow → fast), predicate pushdown, EXISTS vs IN.