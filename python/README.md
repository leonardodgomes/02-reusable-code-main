# 📘 README — Reusable Python Toolkit

This repository contains a modular, reusable Python toolkit designed to support automation, data processing, file management, synthetic data generation, email automation, and general utilities.
Each folder represents a self‑contained module with a clear responsibility, making the project easy to maintain, extend, and reuse across different projects.

## 📁 Project Structure Overview

```
python/
│
├── calculations/
├── data_generators/
── email/
├── file_system/
├── io/
├── utils/
│
└── sandbox.ipynb
```

## 🧮 calculations/

Mathematical and analytical functions used across projects.

**Includes:**

- stats.py — mean, median, variance, and other statistical utilities
- finance.py — financial formulas (NPV, IRR, interest, amortization)
- time_series.py — time‑series helpers (moving averages, smoothing)
- actuarial_age.py — actuarial age calculations
- README.md — module documentation

**Use case:**  
Reusable math logic for analytics, dashboards, and ETL pipelines.


## 🧪 data_generators/
Synthetic data generators for testing, prototyping, and demos.

**Includes:**

- generators.py — general fake datasets (people, sales, random numbers)
- financial_generator.py — stock prices, crypto, transactions, invoices
- create_random_clothes_dataset.py — clothing catalog generator
- create_random_store_dataset.py — store/product dataset generator
- README.md — module documentation

**Use case:**
Quickly generate realistic datasets without relying on real data.


## 📧 email/
Email automation using Outlook + HTML templates.

**Includes:**
- email.py — loads HTML templates, injects placeholders, sends emails
- templates/email_template.html — reusable HTML email layout
- README.md — module documentation

**Features:**
- Dynamic placeholders (e.g., {{greeting}}, {{name}})
- Outlook automation via win32com
- Optional attachments
- Project‑specific email workflows

**Use case:**
Automated reports, notifications, and communication workflows.


## 📂 file_system/
Tools for interacting with the file system.

**Includes:**
- file_system.py — rename files, sanitize names, timestamps
- change_file_names.py — batch rename scripts
- list_files_in_folder.py — folder inspection
- get_path_script.py — path utilities
- get_folders_names_export_to_excel.py — export folder names
- README.md — module documentation

**Use case:**  
File cleanup, organization, and automation tasks.


## 🔄 io/
Input/output utilities and file format converters.

**Includes:**
- io_utils.py — read/write text, JSON, CSV
- file_converters.py — Excel → CSV, CSV → TXT, CSV → Parquet, etc.

**Use case:**  
Standardized data ingestion and export across projects.


## 🛠️ utils/
General helper functions used across modules.

**Includes:**

- determine_operating_system.py — OS detection
- progressing_animation.py — CLI progress animation
- scheduler.py — simple task scheduler
- README.md — module documentation

**Use case:**  
Small utilities that don’t belong to a specific domain.


## 🧪 sandbox.ipynb
A dedicated environment for testing modules during development.

**Use case:**  
Run isolated tests, validate functions, and experiment with new features.


## 🚀 How to Use This Toolkit
1. Clone the repository
2. Open the python/ folder in VS Code
3. Use sandbox.ipynb or sandbox.py to test modules
4. Import modules like:
   ```
    from file_system.file_system import bulk_rename_files
    from data_generators.financial_generator import generate_stock_prices
    from io.file_converters import excel_to_csv
    from email.email import send_email

   ```