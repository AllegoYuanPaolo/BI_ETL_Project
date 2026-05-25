from utils.dbOps import get_db_connection
from etl import ext_trans as src
from models import dest_models as dst
from utils.logger import get_logger

from sqlalchemy import text
from sqlalchemy.orm import InstrumentedAttribute, Session
from typing import Type

log = get_logger(__name__)

def clear_tables_all(session: Session):
    log.info("Clearing all destination tables...")
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
    log.info("All tables cleared successfully.")
    
def clear_table_one(conn: Session, fact_table: Type[dst.Base], dim_table: Type[dst.Base]):
    fact_name = fact_table.__tablename__
    dim_name = dim_table.__tablename__

    try:
        log.info(f"Clearing tables: {fact_name}, {dim_name}")
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))

        conn.execute(text(f"TRUNCATE TABLE {fact_name}"))
        conn.execute(text(f"TRUNCATE TABLE {dim_name}"))

        conn.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
        
        conn.commit()
        log.info(f"Successfully truncated {fact_name} and {dim_name}")
    except Exception as err:
        conn.rollback()
        log.error(f"Error clearing tables: {err}")


#                   === LOAD FUNCS ===
# Flow:
#   Extract transformed data -> truncate destination table -> load data

dest_conn = get_db_connection('orderStatistics')

def load_city_revenue():
    try:
        log.info("Starting City Revenue Load...")
        clear_table_one(dest_conn, dst.FactSales, dst.DimSales)
        data = src.get_cities_revenue()
        
        for item in data.keys():
            dimRow = dst.DimSales(
                customer_city=item
            )
            dest_conn.add(dimRow)
            dest_conn.flush()

            loc_id = dimRow.location_id

            factRow = dst.FactSales(
                    location_id=loc_id,
                    total_revenue=data[item].get('total_revenue'),
                    total_orders=data[item].get('total_orders')
            )
            dest_conn.add(factRow)
        
        dest_conn.commit()
        log.info(f"City Revenue Load complete. Loaded {len(data)} records.")
    except Exception as e:
        dest_conn.rollback()
        log.error(f"Failed to load city revenue: {e}")

def load_product_revenue():
    try:
        log.info("Starting Product Revenue Load...")
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
        log.info(f"Product Revenue Load complete. Loaded {len(data)} records.")
    except Exception as e:
        dest_conn.rollback()
        log.error(f"Failed to load product revenue: {e}")

def load_office_revenue():
    try:
        log.info("Starting Office Revenue Load...")
        clear_table_one(dest_conn, dst.FactOfficeSales, dst.DimOfficeSales)
        data = src.get_office_revenue()
        
        for item in data.keys():
            dimRow = dst.DimOfficeSales(
                office_code=data[item].get('office_code'),
                office_city=item
            )

            dest_conn.add(dimRow)

            factRow = dst.FactOfficeSales(
                office_code=data[item].get('office_code'),
                total_revenue=data[item].get('total_revenue'),
                total_orders=data[item].get('total_orders')
            )

            dest_conn.add(factRow)

        dest_conn.commit()
        log.info(f"Office Revenue Load complete. Loaded {len(data)} records.")
    except Exception as e:
        dest_conn.rollback()
        log.error(f"Failed to load office revenue: {e}")

def load_employee_revenue():
    try:
        log.info("Starting Employee Revenue Load...")
        clear_table_one(dest_conn, dst.FactEmployeeRevenue, dst.DimEmployeeRevenue)
        data = src.get_employee_revenue()
        
        for item in data.keys():
            dimRow = dst.DimEmployeeRevenue(
                employee_number=item,
                employee_name=data[item].get('employee_name'),
                office_city=data[item].get('office_city')
            )
            dest_conn.add(dimRow)

            factRow = dst.FactEmployeeRevenue(
                employee_number=item,
                office_code=data[item].get('office_code'),
                total_revenue=data[item].get('total_revenue'),
                total_orders=data[item].get('total_orders')
            )

            dest_conn.add(factRow)

        dest_conn.commit()
        log.info(f"Employee Revenue Load complete. Loaded {len(data)} records.")
    except Exception as e:
        dest_conn.rollback()
        log.error(f"Failed to load employee revenue: {e}")

def load_prodLine_revenue():
    try:
        log.info("Starting Product Line Revenue Load...")
        clear_table_one(dest_conn, dst.FactProductLineRevenue, dst.DimProductLineRevenue)
        data = src.get_product_line_rev()

        for item in data.keys():
            dimRow = dst.DimProductLineRevenue(
                product_line=item,
                product_line_description=data[item].get('description', 'No description available')
            )

            dest_conn.add(dimRow)

            factRow = dst.FactProductLineRevenue(
                product_line=item,
                total_revenue=data[item].get('total_revenue'),
                total_orders=data[item].get('total_sold')
            )

            dest_conn.add(factRow)
        
        dest_conn.commit()
        log.info(f"Product Line Revenue Load complete. Loaded {len(data)} records.")
    except Exception as e:
        dest_conn.rollback()
        log.error(f"Failed to load product line revenue: {e}")

def load_data():
    load_city_revenue()
    load_product_revenue()
    load_office_revenue()
    load_employee_revenue()
    load_prodLine_revenue()



if __name__ == "__main__":
    load_data()