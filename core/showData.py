from utils import dbOps
from models import dest_models as dst
from sqlalchemy import select, desc, func


def _print_shallow_dict(data: list[dict]):
    for element in data:
        for key, value in element.items():
            print(f"{key} : {value}")
        print()
    ...

def aov(revenue: float, orders: int)->float:
    return round((revenue / orders), 2) if orders > 0 else 0

conn = dbOps.get_db_connection('orderStatistics')

def city_revenue():
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
        {
            "city": row.customer_city,
            "total_revenue": row.total_revenue,
            "total_orders": row.total_orders,
            "average_order_value": aov(row.total_revenue , row.total_orders)
        } for row in results
    ]

def product_revenue():
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
        {
            "product": r.product_name,
            "total_revenue": r.total_revenue,
            "total_orders": r.total_orders,
            "aov": aov(r.total_revenue, r.total_orders)
        } for r in results
    ]

def office_revenue():
    pass

def employee_revenue():
    pass

def productline_revenue():
    pass


if __name__ == "__main__":
    _print_shallow_dict(city_revenue())
    ...