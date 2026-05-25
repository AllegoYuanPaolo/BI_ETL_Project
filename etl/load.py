from utils.dbOps import get_db_connection
from etl import ext_trans as src
from models import dest_models as dst

from sqlalchemy import text
from sqlalchemy.orm import InstrumentedAttribute, Session
from typing import Type

def clear_tables_all(session: Session):
    session.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
    tables = ['dim_employee_revenue', 'dim_office_sales', 
              'dim_product_line_revenue', 'dim_product_sales', 
              'dim_sales', 'fact_employee_revenue', 
              'fact_office_sales', 
              'fact_product_line_revenue', 'fact_product_sales', 
              'fact_sales'
            ]
    
    for table in tables:
        session.execute(text(f"TRUNCATE TABLE {table}"))
    
    
    session.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
    session.commit()
    
def clear_table_one(conn: Session, fact_table: Type[dst.Base], dim_table: Type[dst.Base]):
    fact_name = fact_table.__tablename__
    dim_name = dim_table.__tablename__

    try:
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))

        conn.execute(text(f"TRUNCATE TABLE {fact_name}"))
        conn.execute(text(f"TRUNCATE TABLE {dim_name}"))

        conn.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
        
        conn.commit()
        print("Tables cleared successfully!")
    except Exception as err:
        conn.rollback()
        print(f"Error: {err}")


#                   === LOAD FUNCS ===
# Flow:
#   Extract transformed data -> truncate destination table -> load data

dest_conn = get_db_connection('orderStatistics')

def load_city_revenue():
    clear_table_one(dest_conn, dst.FactSales, dst.DimSales)
    data = src.get_cities_revenue()
    
    for item in data.keys():
        dimRow = dst.DimSales(
            customer_city=item
        )
        print(dimRow.customer_city)
        dest_conn.add(dimRow)
        dest_conn.flush()

        loc_id = dimRow.location_id

        print(f"location ID: {loc_id}")

        factRow = dst.FactSales(
                location_id=loc_id,
                total_revenue=data[item].get('total_revenue'),
                total_orders=data[item].get('total_orders')
        )
        print(factRow.total_revenue, ",", factRow.total_orders)
        print()
        
        dest_conn.add(factRow)
    dest_conn.commit()
    ...

def load_product_revenue():
    clear_table_one(dest_conn, dst.FactProductSales, dst.DimProductSales)
    data = src.get_product_revenue()

    for item in data.keys():
        dimRow = dst.DimProductSales(
            product_code=data[item].get('product_code'),
            product_name=item
        )

        dest_conn.add(dimRow)

        factRow = dst.FactProductSales(
            product_code = data[item].get('product_code'),
            total_revenue=data[item].get('total_revenue'),
            total_orders=data[item].get('total_orders')
        )

        dest_conn.add(factRow)
    
    dest_conn.commit()
    ...

def 



if __name__ == "__main__":
    load_product_revenue()
    ...