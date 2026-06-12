SELECT 
    o.orderDate,
    c.city,
    p.productName, 
    p.msrp,
    sum(od.quantityOrdered) as items_sold,
    p.msrp * sum(od.quantityOrdered) as total_item_revenue

FROM products p
    JOIN orderDetails od
    ON od.productCode = p.productCode
    
    JOIN orders o
    ON o.orderNumber = od.orderNumber

    JOIN customers c
    ON o.customerNumber = c.customerNumber

WHERE o.orderDate = '2025-09-16'

GROUP BY p.productName, o.orderDate

ORDER BY total_item_revenue DESC;


