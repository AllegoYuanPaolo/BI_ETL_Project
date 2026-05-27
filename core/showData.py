from utils import dbOps
from models import dest_models as dst
from sqlalchemy import select, desc, func
import schemas.APIContracts as contract


def data_dump(dataList: list)->None:
    for item in dataList:
        print(item.model_dump())

conn = dbOps.get_db_connection('orderStatistics')

def city_revenue()->list[contract.CityRevenue]:
    stmt = (
        select(
            dst.FactSales.total_revenue,
            dst.FactSales.total_orders,
            dst.DimSales.customer_city,
        )
        .join(dst.DimSales)
        .group_by(dst.DimSales.customer_city)
        .order_by(desc(dst.FactSales.total_revenue))
    )
    results = conn.execute(stmt)

    return [
        contract.CityRevenue(
            city=row.customer_city,
            total_revenue=row.total_revenue,
            total_orders=row.total_orders
        ) for row in results
    ]

def product_revenue()->list[contract.ProductRevenue]:
    stmt = (
        select(
            dst.FactProductSales.total_revenue,
            dst.FactProductSales.total_orders,
            dst.DimProductSales.product_name
        )
        .join(dst.DimProductSales)
        .group_by(dst.DimProductSales.product_name)
        .order_by(desc(dst.FactProductSales.total_revenue))
    )

    results = conn.execute(stmt).all()

    return [
        contract.ProductRevenue(
            product=r.product_name,
            total_orders=r.total_orders,
            total_revenue=r.total_revenue
        ) for r in results
    ]

def office_revenue()->list[contract.OfficeRevenue]:
    stmt = (
        select(
            dst.FactOfficeSales.total_revenue,
            dst.FactOfficeSales.total_orders,
            dst.DimOfficeSales.office_city
        )
        .join(dst.DimOfficeSales)
        .group_by(dst.DimOfficeSales.office_city)
        .order_by(desc(dst.FactOfficeSales.total_revenue))
    )

    results = conn.execute(stmt).all()

    return [
        contract.OfficeRevenue(
            office_city=r.office_city,
            total_orders=r.total_orders,
            total_revenue=r.total_revenue
        ) for r in results
    ]

def employee_revenue()->list[contract.EmployeeRevenue]:
    stmt = (
        select(
            dst.FactEmployeeRevenue.total_orders,
            dst.FactEmployeeRevenue.total_revenue,
            dst.DimEmployeeRevenue.employee_name,
            dst.DimEmployeeRevenue.employee_number,
            dst.DimEmployeeRevenue.office_city
        )
        .join(dst.DimEmployeeRevenue)
        .group_by(dst.DimEmployeeRevenue.employee_number)
        .order_by(desc(dst.FactEmployeeRevenue.total_revenue))
    )

    results = conn.execute(stmt).all()

    return [
        contract.EmployeeRevenue(
            employee_number=r.employee_number,
            employee_name=r.employee_name,
            total_orders=r.total_orders,
            total_revenue=r.total_revenue,
            office_city=r.office_city
        ) for r  in results
    ]
    ...

def productline_revenue()->list[contract.ProductLineRevenue]:
    stmt = (
        select (
            dst.FactProductLineRevenue.total_orders,
            dst.FactProductLineRevenue.total_revenue,
            dst.FactProductLineRevenue.product_line,
            dst.DimProductLineRevenue.product_line_description,
        )
        .join(dst.DimProductLineRevenue)
        .group_by(dst.FactProductLineRevenue.product_line)
        .order_by(desc(dst.FactProductLineRevenue.total_revenue))
    )
    results = conn.execute(stmt).all()

    return [
        contract.ProductLineRevenue(
            product_line=r.product_line,
            description=r.product_line_description,
            total_revenue=r.total_revenue,
            total_orders=r.total_orders
        ) for r in results
    ]


if __name__ == "__main__":
    data_dump(city_revenue())
    ...