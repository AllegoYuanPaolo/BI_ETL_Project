from utils import dbOps

try:
    db = dbOps.get_db_connection('orderStatistics')
    print("Connected Successfully!")
except Exception as err:
    print(f"ERROR: {err}")