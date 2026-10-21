-- Country performance, ranked by sales value.
SELECT
    country,
    COUNT(DISTINCT invoice_no) AS order_count,
    SUM(quantity) AS units_sold,
    ROUND(SUM(quantity * unit_price), 2) AS sales_value
FROM retail_sales
WHERE invoice_no NOT LIKE 'C%'
    AND quantity > 0
    AND unit_price > 0
GROUP BY country
ORDER BY sales_value DESC;
