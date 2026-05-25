SELECT 
    c.city, 
    SUM(o.total_price) AS total_revenue, COUNT(DISTINCT o.orderNumber) AS total_orders,
    SUM(o.total_price) / COUNT(DISTINCT o.orderNumber) AS average_revenue_per_order
FROM customers c

JOIN orders o 
    ON c.customerNumber = o.customerNumber

GROUP BY c.city
ORDER BY total_revenue DESC;

SELECT 
    COUNT(o.orderNumber) AS total_orders
FROM customers c
JOIN orders o 
    ON c.customerNumber = o.customerNumber;
