# 🧰 Reusable Code Library  
### Modular, Production‑Inspired Utilities for Data Engineering, Databricks, and Analytics

This repository contains a curated collection of reusable, production‑ready code modules designed to support data engineering, analytics engineering, and technical demo workflows.  
It reflects modern engineering practices: modular design, clear separation of concerns, and practical utilities that accelerate real‑world development.

The goal is simple:  
**Build once. Reuse everywhere.**

---

# 🌳 Repository Structure
```
02-reusable-code/
│
├── python/
│   │
│   ├── data_generation/
│   ├── calculations/
│   ├── file_system/
│   ├── io/
│   ├── email/
│   ├── utils/
│   │
│   └── README.md
│
├── pyspark/
│   ├── transformations/
│   ├── validations/
│   ├── schema/
│   ├── io/
│   │
│   └── README.md
│
├── databricks/
│   ├── jobs/
│   ├── clusters/
│   ├── notebooks/
│   ├── helpers/
│   │
│   └── README.md
│
├── powerbi/
│   ├── dax/
│   ├── templates/
│   │
│   └── README.md
│
├── sql/
│   ├── analytics/
│   ├── ddl/
│   ├── dml/
│   └── performance/
│   
└── README.md
```


# 🐍 Python Modules

## 📦 data_generation  
Synthetic data generators for demos, testing, and SE scenarios.

**Included:**
- Random clothes dataset generator  
- Random store dataset generator  

**Planned additions:**
- Customer profiles  
- Transactions  
- IoT sensor streams  
- Clickstream events  
- Time‑series with anomalies  

---

## 🧮 calculations  
Reusable business logic and analytical formulas.

**Included:**
- Actuarial age calculation  

**Planned additions:**
- Date dimension generator  
- Financial metrics (CAGR, DCF, moving averages)  
- Customer metrics (CLV, RFM)  
- Statistical utilities (z‑score, outlier detection)  

---

## 📁 file_system  
Utilities for interacting with the file system.

**Included:**
- Bulk file renaming  
- Folder listing  
- Path utilities  
- Export folder names to Excel  

**Planned additions:**
- Directory watcher  
- File hashing  
- Recursive metadata scanner  
- Safe delete/archive utilities  

---

## ✉️ email  
Email utilities for automation and notifications.

**Included:**
- Email sender  
- HTML template  

**Planned additions:**
- Attachment support  
- SMTP config loader  
- Slack/Teams notification sender  

---

## 🛠️ utils  
General-purpose utilities.

**Included:**
- OS detection  
- Progress animation  
- Scheduler  
- Text‑to‑speech  

**Planned additions:**
- Logging wrapper  
- Config loader  
- Retry decorator  
- Timer decorator  
- Exception handler decorator  
- In‑memory caching  

---

# 🔥 PySpark Modules

## 🔄 transformations  
Reusable transformations for Spark DataFrames.

**Planned:**
- Column renaming patterns  
- Null handling utilities  
- String cleaning  
- Date/time transformations  
- JSON flattening  

---

## 🧪 validations  
Data quality and validation utilities.

**Planned:**
- Schema validation  
- Null checks  
- Range checks  
- Referential integrity checks  
- Rule‑based DQ engine  

---

## 📐 schema  
Schema helpers for Spark and Delta.

**Planned:**
- Schema inference  
- Schema comparison  
- Schema evolution utilities  

---

## 📥 io  
I/O helpers for Spark and Delta Lake.

**Planned:**
- Auto Loader wrapper  
- Delta read/write helpers  
- Partitioning utilities  
- Checkpoint path generator  

---

# 🧱 Databricks Modules

## 🧩 jobs  
Templates and helpers for Databricks Jobs API.

## ⚙️ clusters  
Cluster configuration templates.

## 📓 notebooks  
Reusable notebook templates.

## 🧰 helpers  
Utilities for interacting with the Databricks workspace.

---

# 📊 Power BI Modules

## 📐 dax  
Reusable DAX measures and patterns.

## 🎨 templates  
Templates for semantic models and themes.

## 📊 Projects
A collection of complete Power BI solution


# 🗄️ SQL Modules

###🧱 ddl
Definitions for schemas, tables, views, constraints, and structural objects.

###🔧 dml
Reusable patterns for data manipulation, cleansing, loading, and transformations.

### 📊 analytics
Advanced analytical SQL templates for KPIs, time‑series, customer metrics, and feature engineering.

###⚡ performance
Optimization patterns for indexing, partitioning, query tuning, and execution‑plan analysis.


---

# 🧠 Philosophy  
This repository is built with a senior‑level mindset:

- **Modular** → each folder solves one problem  
- **Extensible** → easy to add new utilities  
- **Practical** → based on real engineering needs  
- **Demo‑friendly** → supports SE workflows  
- **Production‑inspired** → follows industry patterns  

It’s a living library — continuously improved as new patterns emerge.




