from utils.dbOps import get_db_connection
from models.auto_generated import Customers, Orders

def test_auto_models():
    # 1. Connect to the DB
    db = get_db_connection("ordertracking")
    
    try:
        # 2. Fetch a customer using the auto-generated 'Customers' class
        # Note: Auto-generated names are often plural
        customer = db.query(Customers).first()
        
        if customer:
            print(f"--- Testing Auto-Generated Models ---")
            print(f"Customer: {customer.customerName}")
            
            # 3. Access the relationship
            # Note: sqlacodegen-v2 named this 'orders_collection' or 'orders' 
            # based on the table name. In your auto_generated.py, it's likely 'orders'
            print(f"Orders found: {len(customer.orders)}")
            
            for order in customer.orders[:3]: # Show first 3
                print(f"  - Order #{order.orderNumber} (Status: {order.status})")
        else:
            print("No customers found in the database.")
            
    except Exception as e:
        print(f"Error testing auto-models: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_auto_models()
