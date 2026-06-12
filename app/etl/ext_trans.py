from datetime import date
from decimal import Decimal
from typing import List

from sqlalchemy import func, select
from sqlalchemy.orm import joinedload

from models import src_models as src
from utils import dbOps
from utils.logger import get_logger

log = get_logger(__name__)
conn = dbOps.get_db_connection('orderTracking')


def get_sales_data() -> List[dict]:
    """
    Extracts every order-detail line joined with customer, employee,
    office, product and product-line data for the star-schema fact table.

    Returns a list of dicts, each containing:
        order_id, order_date, city_name, office_city,
        sales_rep_name, product_name, product_line,
        revenue (priceEach * quantityOrdered), quantity
    """
    try:
        log.info("Extracting order-level sales data...")
        stmt = (
            select(
                src.OrderDetail.orderNumber,
                src.Order.orderDate,
                src.Customer.city,
                src.Office.city.label('office_city'),
                func.concat(src.Employee.firstName, ' ', src.Employee.lastName).label('sales_rep_name'),
                src.Product.productName,
                src.ProductLine.productLine,
                (src.OrderDetail.priceEach * src.OrderDetail.quantityOrdered).label('revenue'),
                src.OrderDetail.quantityOrdered,
            )
            .select_from(src.OrderDetail)
            .join(src.Order, src.OrderDetail.orderNumber == src.Order.orderNumber)
            .join(src.Customer, src.Order.customerNumber == src.Customer.customerNumber)
            .join(src.Employee, src.Customer.salesRepEmployeeNumber == src.Employee.employeeNumber)
            .join(src.Office, src.Employee.officeCode == src.Office.officeCode)
            .join(src.Product, src.OrderDetail.productCode == src.Product.productCode)
            .join(src.ProductLine, src.Product.productLine == src.ProductLine.productLine)
        )

        results = conn.execute(stmt).all()
        log.info(f"Successfully extracted {len(results)} order-detail rows.")

        return [
            {
                "order_id": row.orderNumber,
                "order_date": row.orderDate,
                "city_name": row.city,
                "office_city": row.office_city,
                "sales_rep_name": row.sales_rep_name,
                "product_name": row.productName,
                "product_line": row.productLine,
                "revenue": float(row.revenue),
                "quantity": int(row.quantityOrdered),
            }
            for row in results
        ]
    except Exception as e:
        log.error(f"Error extracting sales data: {e}")
        return []


def _print_data(data: List[dict], mustLog: bool = True) -> None:
    logger_fn = log.info if mustLog else print
    logger_fn("Printing extracted data summary...")
    for row in data:
        logger_fn(f"Order {row['order_id']}: {row['product_name']} x{row['quantity']} = {row['revenue']:,.2f}")


if __name__ == "__main__":
    _print_data(get_sales_data())
