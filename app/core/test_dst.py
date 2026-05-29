from utils import dbOps
from etl.ext_trans import *
from models.dest_models import *
from sqlalchemy import text 
from sqlalchemy.orm import InstrumentedAttribute

def list_tables():
    table_res = conn.execute(text("SHOW TABLES;"))
    tables = [table[0] for table in table_res]
    return tables




if __name__ == "__main__":
    conn = dbOps.get_db_connection('orderStatistics')
    # print(list_tables())
    ...