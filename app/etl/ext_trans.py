from utils import dbOps 
from sqlalchemy.orm import Session
from sqlalchemy import func, select, desc, asc
from models import src_models as src
from typing import DefaultDict
from utils.logger import get_logger

log = get_logger(__name__)
conn = dbOps.get_db_connection('orderTracking')

def get_cities_revenue()->dict:
    '''
    Extracts the total revenue and total orders grouped by cities, in descending order
    
    Returns:
        A dictionary of \n
        `{city: {total_orders: int,total_revenue: float}}`
    '''
    try:
        log.info("Extracting cities revenue...")
        stmt = (
            select(
                src.Customer.city,
                func.count(src.Order.orderNumber).label("total_orders"),
                func.sum(src.Order.total_Price).label("total_revenue")
            )
            .join(src.Order)
            .group_by(src.Customer.city)
            .order_by(desc("total_revenue"))
        )

        results = conn.execute(stmt).all()
        log.info(f"Successfully extracted {len(results)} cities.")

        return {
            row.city: {
                "total_orders": int(row.total_orders),
                "total_revenue": float(row.total_revenue)
            }
            
            for row in results
        }
    except Exception as e:
        log.error(f"Error extracting cities revenue: {e}")
        return {}
        
def get_product_revenue()->dict:
    '''
    Returns:
        ```
        { city:{
            product_code: str,
            msrp: float,
            total_orders: int,
            total_revenue: float
            }
        }
        ```
    '''
    try:
        log.info("Extracting product revenue...")
        stmt = (
            select(
                src.Product.productName,
                src.Product.productCode,
                src.Product.MSRP,
                func.sum(src.OrderDetail.quantityOrdered).label("items_sold"),
                (src.Product.MSRP * func.sum(src.OrderDetail.quantityOrdered)).label("total_item_revenue")
            )
            .join(src.OrderDetail)
            .join(src.Order)
            .group_by(src.Product.productName)
            .order_by(desc("total_item_revenue"))
        )

        results = conn.execute(stmt).all()
        log.info(f"Successfully extracted {len(results)} products.")

        return {
            row.productName: {
                "product_code": str(row.productCode),
                "msrp": float(row.MSRP), 
                "total_orders": int(row.items_sold), 
                "total_revenue": float(row.total_item_revenue)
            }
            for row in results
        }
    except Exception as e:
        log.error(f"Error extracting product revenue: {e}")
        return {}
    
def get_office_revenue():
    '''
    Return:
        ```
        {
            office city: {
                office_code: int,
                total_orders: int,
                total_revenue: float(revenue)
            }
        }
        ```
    '''
    try:
        log.info("Extracting office revenue...")
        stmt = (
            select(
                src.Office.city,
                src.Office.officeCode,
                func.sum(src.Order.total_Price).label("office_revenue"),
                func.count(src.Order.orderNumber).label("total_orders")
            )
            .join(src.Employee, src.Employee.officeCode == src.Office.officeCode)
            .join(src.Customer, src.Customer.salesRepEmployeeNumber == src.Employee.employeeNumber)
            .join(src.Order, src.Order.customerNumber == src.Customer.customerNumber)
            .group_by(src.Office.city)
            .order_by(desc("office_revenue"))
        )

        results = conn.execute(stmt).all()
        log.info(f"Successfully extracted {len(results)} offices.")

        return {
            row.city: {
                 "office_code": row.officeCode,
                 "total_orders": int(row.total_orders),
                 "total_revenue": float(row.office_revenue)
                }
            for row in results
        }
    except Exception as e:
        log.error(f"Error extracting office revenue: {e}")
        return {}

def get_employee_revenue():
    try:
        log.info("Extracting employee revenue...")
        stmt = (
            select(
                src.Employee.employeeNumber,
                func.concat(src.Employee.firstName, ' ', src.Employee.lastName).label('employee_name'),
                src.Office.city.label('office_city'),
                src.Office.officeCode,
                func.sum(src.Order.total_Price).label('total_revenue'),
                func.count(src.Order.orderNumber).label('total_orders')
            )
            .join(src.Customer, src.Customer.salesRepEmployeeNumber == src.Employee.employeeNumber)
            .join(src.Order, src.Order.customerNumber == src.Customer.customerNumber)
            .join(src.Office, src.Office.officeCode == src.Employee.officeCode)
            .group_by(src.Employee.employeeNumber)
        )
        results = conn.execute(stmt).all()
        log.info(f"Successfully extracted {len(results)} employees.")
        
        return {
            row.employeeNumber: {
                "employee_name": row.employee_name,
                "office_city": row.office_city,
                "office_code": row.officeCode,
                "total_revenue": float(row.total_revenue),
                "total_orders": int(row.total_orders)
            } for row in results
        }
    except Exception as e:
        log.error(f"Error extracting employee revenue: {e}")
        return {}

def get_product_line_rev():
    '''
    Returns:
        ```
            { productLine:{
                total_orders: int,
                total_sold: int,
                total_revenue: float
                }
            }
        ```
    '''
    try:
        log.info("Extracting product line revenue...")
        stmt = (
            select(
                src.ProductLine.productLine,
                func.count(src.OrderDetail.productCode).label('total_orders'),
                func.sum(src.OrderDetail.quantityOrdered).label('total_sold'),
                func.sum(src.OrderDetail.priceEach * src.OrderDetail.quantityOrdered).label('total_revenue')
            )
            .join(src.Product, src.ProductLine.productLine == src.Product.productLine)
            .join(src.OrderDetail, src.OrderDetail.productCode == src.Product.productCode)
            .group_by(src.ProductLine.productLine)
            .order_by(desc('total_revenue'))
        )

        results = conn.execute(stmt).all()
        log.info(f"Successfully extracted {len(results)} product lines.")

        return {
            row.productLine: {
                "total_orders": int(row.total_orders),
                "total_sold": int(row.total_sold),
                "total_revenue": float(row.total_revenue)
            } for row in results
        }
    except Exception as e:
        log.error(f"Error extracting product line revenue: {e}")
        return {}

def _print_data(data, mustLog: bool = True)->None:
    if mustLog:
        log.info("Printing extracted data summary...")
        for key, value in data.items():
            if type(value) == dict: 
                log.info(f"Primary Key: {key}")
                for valKey, valVal in value.items():
                    if type(valVal) == float:
                        valVal = f"{valVal:,.2f}"
                    log.info(f"  {valKey}: {valVal}")
            else:
                if type(value) == float:
                        value = f"{value:,.2f}"
                log.info(f"{key}: {value}")
    else:
        for key, value in data.items():
            if type(value) == dict: 
                print(f"Primary Key: {key}")
                for valKey, valVal in value.items():
                    if type(valVal) == float:
                        valVal = f"{valVal:,.2f}"
                    print(f"    {valKey}: {valVal}")
            else:
                if type(value) == float:
                        value = f"{value:,.2f}"
                print(f"{key}: {value}")

if __name__ == "__main__":
    _print_data(get_office_revenue())
