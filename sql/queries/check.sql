-- select
--     pl.productLine,
--     count(od.productCode) as total_orders
-- FROM productLines as pl
-- JOIN products as p
--     ON pl.productLine = p.productLine
-- JOIN orderDetails as od
--     ON p.productCode = od.productCode
-- GROUP BY pl.productLine;


select sum(total_orders)
FROM (
    select
        count(od.productCode) as total_orders
    FROM productLines as pl
    JOIN products as p
        ON pl.productLine = p.productLine
    JOIN orderDetails as od
        ON p.productCode = od.productCode
    GROUP BY pl.productLine
) as ord_count;