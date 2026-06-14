SELECT 
    o.orderDate, 
    c.city, 
    SUM(o.total_Price) as revenue,
    COUNT(DISTINCT o.orderNumber) as sales
FROM customers as c
    JOIN orders as o
    ON o.customerNumber = c.customerNumber
GROUP BY c.city, o.orderDate
