-- Basic quality checks for the cleaned sales table.
SELECT
    'row_count' AS check_name,
    COUNT(*) AS check_value
FROM retail_sales

UNION ALL

SELECT
    'missing_invoice_no',
    COUNT(*)
FROM retail_sales
WHERE invoice_no IS NULL
    OR TRIM(invoice_no) = ''

UNION ALL

SELECT
    'nonpositive_quantity',
    COUNT(*)
FROM retail_sales
WHERE quantity <= 0

UNION ALL

SELECT
    'nonpositive_unit_price',
    COUNT(*)
FROM retail_sales
WHERE unit_price <= 0


UNION ALL

SELECT
    'missing_customer_id',
    COUNT(*)
FROM retail_sales
WHERE customer_id IS NULL
    OR TRIM(CAST(customer_id AS TEXT)) = '';

