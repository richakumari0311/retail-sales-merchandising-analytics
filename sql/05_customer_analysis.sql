-- Customer analysis excludes rows without a customer ID.
WITH customer_orders AS (
    SELECT
        customer_id,
        COUNT(DISTINCT invoice_no) AS order_count,
        SUM(quantity * unit_price) AS customer_sales
    FROM retail_sales
    WHERE invoice_no NOT LIKE 'C%'
        AND quantity > 0
        AND unit_price > 0
        AND customer_id IS NOT NULL
        AND TRIM(CAST(customer_id AS TEXT)) <> ''
    GROUP BY customer_id
)
SELECT
    COUNT(*) AS identified_customers,
    SUM(CASE WHEN order_count > 1 THEN 1 ELSE 0 END)
        AS repeat_customers,
    ROUND(
        100.0 * SUM(
            CASE WHEN order_count > 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS repeat_customer_pct,
    ROUND(AVG(customer_sales), 2) AS avg_sales_per_customer
FROM customer_orders;
