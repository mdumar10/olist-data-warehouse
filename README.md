# Olist Data Warehouse

An end-to-end Data Warehouse project built using **Python** and **Pandas** following the **Medallion Architecture (Bronze → Silver → Gold)**.

The goal of this project was to understand how a real ETL pipeline is designed, how raw data moves through different layers, and how a Star Schema is created for analytics.

---

# Project Overview

The pipeline starts with raw CSV files from the Olist Brazilian E-commerce dataset.

The data goes through three layers:

* **Bronze** → Raw data converted to Parquet
* **Silver** → Cleaned and standardized datasets
* **Gold** → Star Schema with Dimension and Fact tables

The final output is an analytics-ready Data Warehouse.

---

# Project Structure

```text
olist-data-warehouse/

├── src/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── utils/
│
├── notebooks/
├── data/
├── output/
│
├── config.py
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

# Pipeline Flow

```
Raw CSV Files
      │
      ▼
 Bronze Layer
      │
      ▼
 Silver Layer
      │
      ▼
  Gold Layer
      │
      ▼
 Star Schema
```

---

# Gold Layer

## Dimension Tables

* dim_customer
* dim_product
* dim_seller
* dim_payment
* dim_date

## Fact Tables

* fact_sales
* fact_payment
* fact_reviews
* fact_delivery

---

# Technologies

* Python
* Pandas
* Parquet
* Git
* GitHub

---

# Running the Project

Clone the repository

```bash
git clone https://github.com/mdumar10/olist-data-warehouse.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the pipeline

```bash
python run_pipeline.py
```

The pipeline automatically executes:

1. Bronze Layer
2. Silver Layer
3. Gold Layer

---

# Dataset

This project uses the **Olist Brazilian E-Commerce Public Dataset**.

The dataset is not included in this repository because of its size.

Download it from:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

# What I Learned

This project helped me understand:

* Building an ETL pipeline from scratch
* Organizing code into Bronze, Silver and Gold layers
* Cleaning and transforming real-world data
* Working with Parquet files
* Creating Dimension and Fact tables
* Designing a Star Schema
* Structuring a Python project
* Using Git and GitHub in a real project

---

# Future Improvements

The next version of this project will be rebuilt using:

* PySpark
* Spark SQL
* Delta Lake
* Databricks
* Azure

The goal is to compare a Pandas-based ETL pipeline with a Big Data implementation.

---

# Author

**Mohammed Umar Shaikh**

Learning Data Engineering one project at a time.

GitHub:
https://github.com/mdumar10

