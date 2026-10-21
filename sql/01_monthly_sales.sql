-- Monthly sales trend. Sales value is not profit.
SELECT
    strftime('%Y-%m', invoice_date) AS sales_month,
    ROUND(SUM(quantity * unit_price), 2) AS sales_value,
    COUNT(DISTINCT invoice_no) AS order_count,
    SUM(quantity) AS units_sold
FROM retail_sales
WHERE invoice_no NOT LIKE 'C%'
    AND quantity > 0
    AND unit_price > 0
GROUP BY strftime('%Y-%m', invoice_date)
ORDER BY sales_month;
