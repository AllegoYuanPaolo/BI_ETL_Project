SELECT
    ord.orderDate,
    cust.city,
    emp.employeeNumber,
    emp.firstName,
    SUM(ord.total_price) as employee_revenue,
    COUNT(ord.orderNumber) as total_orders

FROM employees AS emp
JOIN customers as cust
    ON cust.salesRepEmployeeNumber = emp.employeeNumber
JOIN orders AS ord
    on cust.customerNumber = ord.customerNumber

WHERE ord.orderDate < '2026-01-01'

GROUP BY emp.employeeNumber;