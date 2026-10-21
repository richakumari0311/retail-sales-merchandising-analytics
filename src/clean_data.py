"""Clean the UCI Online Retail workbook and export analysis-ready CSV files."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
INPUT_FILE = DATA_DIR / "online_retail.xlsx"

EXPECTED_COLUMNS = {
    "invoice_no",
    "stock_code",
    "description",
    "quantity",
    "invoice_date",
    "unit_price",
    "customer_id",
    "country",
}



def normalize_columns(columns):
    """Normalize source column names to the expected schema."""
    normalized = (
        columns.str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )

    column_mapping = {
        "invoiceno": "invoice_no",
        "stockcode": "stock_code",
        "invoicedate": "invoice_date",
        "unitprice": "unit_price",
        "customerid": "customer_id",
    }

    return normalized.to_series().replace(column_mapping).set_axis(columns)



def main():
    """Clean the source workbook and write CSV outputs and a report."""
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Source workbook not found: {INPUT_FILE}. "
            "Download the UCI Online Retail dataset and save it at this path."
        )

    data = pd.read_excel(INPUT_FILE)
    data.columns = normalize_columns(data.columns)

    missing_columns = EXPECTED_COLUMNS - set(data.columns)
    if missing_columns:
        raise ValueError(
            "Source workbook is missing expected columns: "
            f"{sorted(missing_columns)}. Found: {list(data.columns)}"
        )

    initial_rows = len(data)
    duplicate_rows = int(data.duplicated().sum())
    missing_customer_rows = int(data["customer_id"].isna().sum())
    initial_cancellations = data["invoice_no"].astype(str).str.startswith(
        "C", na=False
    )
    cancellation_rows_found = int(initial_cancellations.sum())
    negative_quantity_rows = int((data["quantity"] < 0).sum())
    nonpositive_price_rows = int((data["unit_price"] <= 0).sum())

    data = data.drop_duplicates().copy()
    data["invoice_no"] = data["invoice_no"].astype(str).str.strip()
    data["invoice_date"] = pd.to_datetime(
        data["invoice_date"], errors="coerce"
    )
    data["quantity"] = pd.to_numeric(data["quantity"], errors="coerce")
    data["unit_price"] = pd.to_numeric(data["unit_price"], errors="coerce")
    data["line_value"] = data["quantity"] * data["unit_price"]

    cancellation_mask = data["invoice_no"].str.startswith("C", na=False)
    cancellations = data.loc[cancellation_mask].copy()
    sales_mask = (
        ~cancellation_mask
        & (data["quantity"] > 0)
        & (data["unit_price"] > 0)
        & data["invoice_date"].notna()
    )
    sales = data.loc[sales_mask].copy()

    sales["customer_id"] = sales["customer_id"].astype("Int64")
    cancellations["customer_id"] = cancellations["customer_id"].astype("Int64")

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    sales_path = DATA_DIR / "retail_clean.csv"
    cancellations_path = DATA_DIR / "retail_cancellations.csv"
    sales.to_csv(sales_path, index=False)
    cancellations.to_csv(cancellations_path, index=False)

    report = f"""Retail dataset cleaning report
=============================
Input rows: {initial_rows:,}
Exact duplicate rows found: {duplicate_rows:,}
Rows with missing customer ID before cleaning: {missing_customer_rows:,}
Cancellation rows identified before duplicate removal: {cancellation_rows_found:,}
Rows with negative quantity before cleaning: {negative_quantity_rows:,}
Rows with zero or negative unit price before cleaning: {nonpositive_price_rows:,}
Rows after exact-duplicate removal: {len(data):,}
Analysis-ready sales rows: {len(sales):,}
Cancellation rows exported: {len(cancellations):,}

Sales inclusion rules:
- Invoice number does not begin with C
- Quantity is greater than zero
- Unit price is greater than zero
- Invoice date is valid

Notes:
- Missing customer IDs are retained in sales data and excluded from
  customer-level analysis.
- Cancellation records are exported separately.
- Line value is quantity multiplied by unit price. It is not profit.
"""
    report_path = ROOT / "docs" / "cleaning_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")

    print(report)
    print(f"Created: {sales_path}")
    print(f"Created: {cancellations_path}")


if __name__ == "__main__":
    main()
