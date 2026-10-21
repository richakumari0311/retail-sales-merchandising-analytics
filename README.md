# Retail Sales and Merchandising Analytics

## Overview

This project analyzes the UCI Online Retail transaction dataset to identify sales trends, top-performing stock codes, country-level performance, repeat purchasing, and recorded cancellations.

The analysis uses Python and pandas for data cleaning, SQLite for SQL analysis, and Looker Studio for dashboard visualization. It demonstrates a reproducible workflow from raw transaction data to business insights.

## Tools

- **Python:** Data cleaning and preparation
- **pandas:** Data manipulation
- **SQLite:** SQL analysis and data-quality checks
- **Looker Studio:** Dashboard development
- **Git and GitHub:** Version control and project documentation

## Project Structure

```text
retail-sales-merchandising-analytics/
├── README.md
├── .gitignore
├── src/
│   └── clean_data.py
├── sql/
│   ├── 01_monthly_sales.sql
│   ├── 02_top_products.sql
│   ├── 03_country_performance.sql
│   ├── 04_cancellations.sql
│   ├── 05_customer_analysis.sql
│   └── 06_data_quality_checks.sql
├── docs/
│   ├── business_findings.md
│   ├── data_dictionary.md
│   └── cleaning_report.txt
└── reports/
    └── retail_sales_dashboard.pdf
```

The PDF and screenshot should be listed here only if the files exist at these paths.

## Data Source

The project uses the [UCI Online Retail dataset](https://archive.ics.uci.edu/dataset/352/online+retail).

Download the source Excel workbook and save it locally as:

`data/online_retail.xlsx`

The raw workbook, generated CSV files, and local SQLite database are excluded from GitHub. Users must download the source dataset separately to reproduce the analysis.

## How to Run the Analysis

### 1. Install dependencies

From the project root, run:

```bash
python -m pip install pandas openpyxl
```

SQLite is also required. On macOS, check its availability with:

```bash
sqlite3 --version
```

### 2. Prepare the source data

Create the `data/` directory and place the downloaded Excel workbook at:

```text
data/online_retail.xlsx
```

### 3. Clean the dataset

Run the Python cleaning script from the project root:

```bash
python src/clean_data.py
```

The script generates:

- `data/retail_clean.csv`
- `data/retail_cancellations.csv`

The cleaned sales dataset retains records with missing customer IDs for overall sales analysis. Customer-level analysis excludes both blank and NULL customer IDs.

### 4. Create the SQLite database

For a fresh analysis, create a new database and import the generated CSV files.

**Warning:** The following command removes an existing local database file. Use it only when you intend to rebuild the database.

```bash
rm -f data/retail_sales.db
sqlite3 data/retail_sales.db
```

At the SQLite prompt, import the cleaned sales data:

```sql
.mode csv
.headers on
.import data/retail_clean.csv retail_sales
```

Import the cancellation data into a separate table:

```sql
.import data/retail_cancellations.csv retail_cancellations
```

Exit SQLite:

```sql
.quit
```

The SQL scripts use `retail_sales` for sales analysis and `retail_cancellations` for cancellation analysis.

### 5. Run the SQL queries

Run an individual query from the project root:

```bash
sqlite3 -header -column data/retail_sales.db < sql/01_monthly_sales.sql
```

Replace `01_monthly_sales.sql` with the relevant filename to run another query.

The six SQL scripts cover:

1. Monthly sales trends
2. Top stock codes by sales value
3. Country-level performance
4. Cancellation analysis
5. Customer purchasing behavior
6. Data-quality checks

### 6. Build the dashboard

Connect the cleaned sales data to Looker Studio to build or update the dashboard.

Ensure customer-level metrics exclude blank and NULL customer IDs. Retain those records in the main sales dataset so valid transactions remain available for overall sales reporting.

## Key Findings

- **Recorded sales value:** £10,642,110.80 across 19,960 distinct invoices.
- **Units sold:** 5,572,420 across 524,878 qualifying sales rows.
- **Highest monthly sales value:** November 2011, at £1,503,866.78.
- **Repeat purchasing:** 2,845 of 4,338 identified customers (65.58%) had more than one qualifying invoice.
- **Average sales value per identified customer:** £2,048.69.
- **Geographic performance:** The dataset covers 38 countries, with the United Kingdom recording the highest sales value.
- **Partial reporting period:** December 2011 is incomplete because the source data ends on 9 December 2011.

For further interpretation and suggested follow-up analysis, see [Business Findings](docs/business_findings.md).

## Definitions and Limitations

- **Sales value:** Calculated as `quantity * unit_price`. It represents recorded transaction line value, not profit.
- **Qualifying sales:** Exclude invoices beginning with `C`, nonpositive quantities, nonpositive unit prices, and invalid invoice dates.
- **Missing customer IDs:** Retained in the sales dataset but excluded from customer-level analysis. Both blank strings and SQL NULL values are treated as missing.
- **Repeat customers:** Identified customers with more than one distinct qualifying invoice during the observed dataset period.
- **Cancellation records:** Analyzed separately. Absolute cancellation-line value does not necessarily represent lost revenue or net financial impact.
- **Stock code rankings:** Some stock codes represent postage, manual entries, or other charges rather than physical merchandise.
- **Profit and inventory:** Product costs and inventory levels are not available, so profit margins and stockouts cannot be measured.

See the [Data Dictionary](docs/data_dictionary.md) for field definitions and KPI calculations, and the [Cleaning Report](docs/cleaning_report.txt) for data-preparation details.

## Dashboard Report

## Dashboard Preview

The interactive dashboard was built in Looker Studio. A PDF export is provided for convenient offline preview of the dashboard’s key visualizations and insights.

[View the Dashboard PDF](reports/retail_sales_dashboard.pdf)
