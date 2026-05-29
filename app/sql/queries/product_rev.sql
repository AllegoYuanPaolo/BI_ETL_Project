SELECT 
    p.productName, 
    p.msrp,
    sum(od.quantityOrdered) as items_sold,
    p.msrp * sum(od.quantityOrdered) as total_item_revenue

FROM products p
    JOIN orderDetails od
    ON od.productCode = p.productCode
    
    JOIN orders o
    ON o.orderNumber = od.orderNumber

GROUP BY p.productName
ORDER BY total_item_revenue DESC;


