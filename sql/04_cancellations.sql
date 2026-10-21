-- Run against retail_cancellations.csv imported as retail_cancellations.
-- Cancellation-line value is not necessarily lost revenue or net financial impact.
SELECT
    COUNT(DISTINCT invoice_no) AS cancellation_invoice_count,
    SUM(ABS(quantity)) AS units_in_cancelled_lines,
    ROUND(SUM(ABS(quantity * unit_price)), 2) AS cancellation_line_value
FROM retail_cancellations;
