SELECT
    pl.productLine,
    count(od.productCode) as total_orders,
    sum(od.quantityOrdered) as total_sold,
    sum(od.priceEach * od.quantityOrdered) as total_revenue

FROM productLines as pl

JOIN products as p
    ON pl.productLine = p.productLine
JOIN orderDetails as od
    ON od.productCode = p.productCode

GROUP BY pl.productLine
ORDER BY total_revenue DESC;


sqlacodegen_v2 mysql+pymysql://root:password@localhost/orderStatistics --outfile dest_model.py