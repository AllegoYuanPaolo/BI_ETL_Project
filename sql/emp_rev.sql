SELECT
    emp.employeeNumber,
    emp.firstName,
    SUM(ord.total_price) as employee_revenue,
    COUNT(ord.orderNumber) as total_orders

FROM employees AS emp
JOIN customers as cust
    ON cust.salesRepEmployeeNumber = emp.employeeNumber
JOIN orders AS ord
    on cust.customerNumber = ord.customerNumber

GROUP BY emp.employeeNumber;