-- Top 10 stock codes by sales value. Sales value is not profit.
SELECT
    stock_code,
    MAX(description) AS product_description,
    SUM(quantity) AS units_sold,
    ROUND(SUM(quantity * unit_price), 2) AS sales_value
FROM retail_sales
WHERE invoice_no NOT LIKE 'C%'
    AND quantity > 0
    AND unit_price > 0
GROUP BY stock_code
ORDER BY sales_value DESC
LIMIT 10;
