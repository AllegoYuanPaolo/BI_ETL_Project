from utils import dbOps 
from sqlalchemy.orm import Session
from sqlalchemy import func, select, desc, asc
from models import src_models as src
from typing import DefaultDict

conn = dbOps.get_db_connection('orderTracking')

def get_cities_revenue()->dict:
    '''
    Extracts the total revenue and total orders grouped by cities, in descending order
    
    Returns:
        A dictionary of \n
        `{city: {total_orders: int,total_revenue: float}}`
    '''
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

    return {
        row.city: {
            "total_orders": int(row.total_orders),
            "total_revenue": float(row.total_revenue)
        }
        
        for row in results
    }
        
def get_product_revenue()->dict:
    '''
    
    '''
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

    return {
        row.productName: {
            "product_code": str(row.productCode),
            "msrp": float(row.MSRP), 
            "total_orders": int(row.items_sold), 
            "total_revenue": float(row.total_item_revenue)
        }
        for row in results
    }
    
def get_office_revenue():
    stmt = (
        select(
            src.Office.city,
            func.sum(src.Order.total_Price).label("office_revenue")
        )
        .join(src.Employee, src.Employee.officeCode == src.Office.officeCode)
        .join(src.Customer, src.Customer.salesRepEmployeeNumber == src.Employee.employeeNumber)
        .join(src.Order, src.Order.customerNumber == src.Customer.customerNumber)
        .group_by(src.Office.city)
        .order_by(desc("office_revenue"))
    )

    results = conn.execute(stmt).all()

    return {
        row.city: float(row.office_revenue)
        for row in results
    }
    ...

def get_product_line_rev():
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

    return {
        row.productLine: {
            "total orders": int(row.total_orders),
            "total_sold": int(row.total_sold),
            "total_revenue": float(row.total_revenue)
        } for row in results
    }

def print_data(data)->None:
    for key, value in data.items():
        if type(value) == dict: 
            print(f"Primary Key: {key}:")
            for valKey, valVal in value.items():
                
                if type(valVal) == float:
                    valVal = f"{valVal:,.2f}"
                if type(valVal) == float:
                    valVal = f"{valVal:,.0f}"
                
                print(f"\t{valKey}: {valVal}")
        else:
            if type(value) == float:
                    value = f"{value:,.2f}"
            if type(value) == float:
                    value = f"{value:,.0f}"
            print(f"{key}: {value}")

        print()

if __name__ == "__main__":
    print_data(get_product_revenue())
    
    ...