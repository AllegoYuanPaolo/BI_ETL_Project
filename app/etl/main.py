from etl import load
from utils import dbOps 

def run_etl():
    dest_conn = dbOps.get_db_connection('orderStatistics')

    try: 
        load.load_city_revenue()

        load.load_employee_revenue()

        load.load_office_revenue()

        load.load_prodLine_revenue

        load.load_product_revenue()
    except Exception as err:
        print(f"ERROR: {err}")
    finally:
        dest_conn.close()

if __name__ == "__main__":
    run_etl()
    ...