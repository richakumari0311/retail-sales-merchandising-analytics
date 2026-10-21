# Business Findings: UCI Online Retail Analysis

## 1. Sales Trend

- **Highest monthly sales value:** November 2011, at £1,503,866.78.
- **Lowest monthly sales value:** February 2011, at £522,545.56.
- December 2011 recorded £637,790.33 in sales value. However, the source data ends on 9 December 2011, making December a partial month that should not be compared directly with complete months.
- **Suggested follow-up:** Compare complete months and investigate seasonal demand and order mix before making merchandising decisions.

## 2. Product and Stock Code Performance

- The highest-ranked stock code by recorded sales value was **DOTCOM POSTAGE (stock code DOT)**, with £206,248.77.
- The dataset includes service- and charge-related stock codes, including postage and manual entries. Therefore, rankings by stock code do not represent merchandise-only product rankings.
- **Suggested follow-up:** Separate merchandise from service and charge entries using a documented classification rule. Then compare units sold and sales value for merchandise-only stock codes. Additional inventory data would help investigate assortment and availability.

## 3. Customer Behavior

- Among customers with an identified, nonblank customer ID, **2,845 of 4,339 customers (65.58%)** had more than one qualifying invoice.
- Average recorded sales value per identified customer was £2,048.69.
- The repeat-customer share describes purchasing behavior within the observed dataset period. It is not a cohort retention rate or proof of future loyalty.
- **Suggested follow-up:** Segment customers by recency, frequency, and monetary value (RFM). If additional historical data is available, investigate changes in purchasing behavior over time.

## 4. Cancellation Records

The separate cancellation extract contains:

- **3,836** distinct cancellation invoices.
- **275,560** units across cancellation lines, measured using absolute quantities.
- **£893,979.73** in absolute cancellation-line value.

Cancellation-line value is not necessarily lost revenue or net financial impact. Further transaction-level reconciliation would be needed to determine the financial effect of cancellations.

## 5. Dataset and Cleaning Summary

| Metric | Result |
|---|---:|
| Original rows | 541,909 |
| Exact duplicate rows identified and removed | 5,268 |
| Rows after exact-duplicate removal | 536,641 |
| Analysis-ready sales rows | 524,878 |
| Recorded sales value | £10,642,110.80 |
| Distinct qualifying invoices | 19,960 |
| Units sold | 5,572,420 |
| Identified customers | 4,339 |
| Customers with more than one qualifying invoice | 2,845 |
| Repeat-customer share | 65.58% |
| Countries represented | 38 |

**Qualifying sales date range:** 1 December 2010 to 9 December 2011.

The sales dataset retains transaction rows with missing customer IDs for overall sales analysis. Customer-level analysis excludes both blank and SQL NULL customer IDs. The SQLite quality check identified 132,186 sales rows with missing or blank customer IDs.

## 6. Important Limitations

- Sales value is calculated as quantity multiplied by unit price. It is not profit.
- The source data does not provide product costs or inventory-on-hand data, so profit margins and stockouts cannot be measured.
- Customer IDs are missing or blank on some transaction rows. These rows remain available for overall sales reporting but are excluded from customer-level metrics.
- December 2011 is incomplete in the supplied extract.
- Stock codes can represent merchandise, postage, or other charges. Merchandise-specific conclusions require an explicit classification rule.
- Cancellation-line values should not be interpreted as confirmed lost revenue without additional reconciliation.
