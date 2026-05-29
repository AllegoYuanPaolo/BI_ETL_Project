SELECT
    off.city AS office_loc,
    COUNT(ord.orderNumber) as total_orders,
    SUM(ord.total_price) AS office_revenue

FROM offices AS off

JOIN employees AS e 
    ON off.officeCode = e.officeCode

JOIN customers AS c 
    ON c.salesRepEmployeeNumber = e.employeeNumber

JOIN orders AS ord 
    ON c.customerNumber = ord.customerNumber

GROUP BY off.city
ORDER BY office_revenue DESC;
