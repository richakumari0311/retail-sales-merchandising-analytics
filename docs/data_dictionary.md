# Data Dictionary

## Source Dataset Fields

The source dataset is the UCI Online Retail transaction dataset. The following fields are used in the analysis.

| Field | Meaning | Notes |
|---|---|---|
| `invoice_no` | Invoice or transaction identifier | Values beginning with `C` identify cancellation records in this dataset. |
| `stock_code` | Product or item identifier | Treat as text, not a numeric measure. Some codes represent postage or charges rather than merchandise. |
| `description` | Item description | May contain missing values or inconsistent labels. |
| `quantity` | Units on a transaction line | Negative values may appear in cancellation records. Qualifying sales require positive quantities. |
| `invoice_date` | Transaction date and time | Parsed as a date/time field. Invalid dates are excluded from qualifying sales. |
| `unit_price` | Price per unit | Used with quantity to calculate transaction line value. Only positive prices are included in qualifying sales. |
| `customer_id` | Customer identifier | Some records have missing or blank IDs. These records remain in the sales dataset but are excluded from customer-level analysis. |
| `country` | Country associated with the transaction | Used for geographic grouping and sales comparisons. |
| `line_value` | Derived transaction line value | Calculated as `quantity * unit_price`. It is a sales value proxy, not profit. |

## KPI Definitions

- **Sales value:** Sum of `quantity * unit_price` for qualifying sales rows. Cancellation invoices, nonpositive quantities, nonpositive unit prices, and invalid invoice dates are excluded.
- **Orders:** Count of distinct invoice numbers under the qualifying sales rules.
- **Units sold:** Sum of positive quantities across qualifying sales rows.
- **Identified customers:** Count of distinct, nonblank customer IDs among qualifying sales rows.
- **Repeat customer:** An identified customer with more than one distinct qualifying invoice during the observed dataset period.
- **Repeat-customer share:** Repeat customers divided by identified customers, multiplied by 100.
- **Average sales value per identified customer:** Average of each identified customer's total qualifying sales value. This is not profit or customer lifetime value.
- **Cancellation invoice count:** Number of distinct invoice numbers in the separate cancellation dataset.
- **Units in cancelled lines:** Sum of absolute quantities across cancellation lines.
- **Cancellation-line value:** Sum of the absolute values of `quantity * unit_price` across cancellation lines. This is not necessarily lost revenue or net financial impact.

## Data Cleaning and Inclusion Rules

- Exact duplicate source rows are removed before preparing the analysis datasets.
- Cancellation records are exported separately from qualifying sales rows.
- Qualifying sales exclude invoice numbers beginning with `C`.
- Qualifying sales require positive quantities, positive unit prices, and valid invoice dates.
- Missing customer IDs are retained in the sales dataset to preserve valid transaction records for overall sales reporting.
- Customer-level analysis excludes both SQL `NULL` customer IDs and blank customer ID strings.
- SQLite data-quality checks treat blank and `NULL` customer IDs as missing.

## Verified Analysis Results

The following results were obtained from the cleaned dataset and SQL analysis:

| Metric | Result |
|---|---:|
| Analysis-ready sales rows | 524,878 |
| Distinct qualifying invoices | 19,960 |
| Units sold | 5,572,420 |
| Sales value | £10,642,110.80 |
| Identified customers | 4,339 |
| Repeat customers | 2,845 |
| Repeat-customer share | 65.58% |
| Average sales value per identified customer | £2,048.69 |
| Countries represented | 38 |
| Cancellation invoices | 3,836 |
| Units in cancelled lines | 275,560 |
| Absolute cancellation-line value | £893,979.73 |

## Limitations

- Sales value does not represent profit because product costs and other operating costs are not provided.
- Cancellation-line value should not be interpreted as confirmed lost revenue without additional reconciliation.
- Stock codes may represent merchandise, postage, or other charges.
- Missing customer IDs prevent some transaction rows from being attributed to an individual customer.
- December 2011 is a partial month because the source data ends on 9 December 2011.
