# 🎣 Game Analytics Data Engineering Project

## 📌 Overview

This project demonstrates a **modern data engineering pipeline** built using **Azure Data Lake + Databricks + Delta Lake**.

The pipeline follows a **Medallion Architecture**:

* Bronze → Raw ingestion
* Silver → Cleaned & transformed data
* Gold → Business-ready analytics

---

## 🏗️ Architecture

```
ADLS (Azure Data Lake Storage)
│
├── raw/
├── curated/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
```

---

## ⚙️ Tech Stack

* Azure Data Lake Storage (ADLS Gen2)
* Azure Databricks
* Delta Lake
* PySpark
* Auto Loader
* Unity Catalog

---

## 🔄 Data Pipeline

### 🟤 Bronze Layer

* Ingest data using **Auto Loader**
* Schema inference & evolution
* Incremental file processing

### 🟡 Silver Layer

* Data cleaning & standardization
* Type casting & normalization
* Joins to build **fact table (events)**
* Partitioning by event_date

### 🔵 SCD Handling

* Implemented **SCD Type 1**
* Supports incremental updates using MERGE

### 🟢 Gold Layer

* Aggregated KPIs:

  * Player performance
  * Species success rate
  * Map revenue analysis
  * Daily trends

---

## 📊 Data Model

### Dimension Tables

* Players
* Species
* Maps
* Rods
* Baits

### Fact Table

* Events

---

## 🚀 Key Features

* Incremental ingestion using Auto Loader
* Partitioned Delta tables
* Scalable architecture
* Star schema modeling
* SCD implementation
* Performance optimization (Z-Order, OPTIMIZE)

---

## ⚡ Optimization Techniques

* Partitioning (event_date)
* OPTIMIZE (file compaction)
* Z-ORDER (query performance)
* VACUUM (cleanup)

---

## 📁 Project Structure

```
notebooks/
  ├── bronze ingestion
  ├── silver transformations
  ├── events fact table
  ├── SCD logic
  ├── gold KPIs
  ├── optimization
```

---

## 📌 How to Run

1. Create external locations and catalog
2. Run Bronze ingestion notebook
3. Run Silver transformation notebooks
4. Execute SCD logic
5. Run Gold aggregations
6. Apply optimization

---

## 🎯 Learning Outcomes

* End-to-end data pipeline design
* Medallion architecture implementation
* Delta Lake operations
* SCD concepts
* Performance tuning

---

## 👨‍💻 Author

Sayed Shahrukh Hussainy
