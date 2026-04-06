# Retail Customer Analytics Pipeline

An end-to-end business analytics pipeline built on 550,000+ rows of real Brazilian e-commerce data from Olist (2016–2018).

## Live Dashboard
[View Interactive Tableau Dashboard](https://public.tableau.com/views/OlistE-CommerceAnalyticsDashboard_17754432140590/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Project Overview
This project covers the complete analytics workflow:
- Data ingestion pipeline (Python, PostgreSQL, SQLAlchemy)
- Data cleaning and validation (pandas)
- Advanced SQL analysis (window functions, CTEs, CLV)
- KPI dashboard development
- A/B testing (scipy, p < 0.0001, n = 96,353 orders)
- Customer segmentation (K-Means, RFM model)
- Churn prediction (Logistic Regression, ROC-AUC = 1.0)
- Interactive Tableau dashboard (5 charts)

## Key Findings
- São Paulo drove 47% of total platform revenue (R$5.2M)
- Fast delivery (≤10 days) scored 4.39/5 vs slow delivery 3.94/5 (p < 0.0001)
- 66.6% of customers churned after first purchase
- 3 customer segments identified: Champions (4,962), Loyal Customers (50,830), At Risk (37,566)

## Tech Stack
Python · PostgreSQL · SQL · pandas · scikit-learn · scipy · matplotlib · Tableau · Git

## Project Structure

retail-analytics-pipeline/
├── data/
│   ├── raw/          # Original Olist CSV files
│   ├── cleaned/      # Cleaned datasets
│   └── processed/    # Analysis-ready exports for Tableau
├── notebooks/        # Jupyter analysis notebooks
├── sql/              # Database schema and queries
├── scripts/          # Python ingestion scripts
└── dashboards/       # Saved chart images


## Notebooks
| Notebook | Description |
|----------|-------------|
| 01_data_cleaning | Missing value treatment, type fixing, deduplication |
| 02_advanced_sql_analysis | Window functions, CTEs, revenue trends, CLV |
| 03_kpi_analysis | 6 KPIs + 4-chart dashboard |
| 04_ab_testing | Delivery speed vs review scores experiment |
| 05_machine_learning | K-Means segmentation + churn prediction |

## Author
Meet Patel | M.S. Business Analytics, DePaul University
[LinkedIn](https://linkedin.com/in/meeetppatel) | [GitHub](https://github.com/meeetppatel)

