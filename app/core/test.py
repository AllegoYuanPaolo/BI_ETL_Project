from models.src_models import Customer, Order
from utils.dbOps import get_db_connection
from sqlalchemy.orm import Session
from typing import DefaultDict

def test_customer(db: Session):
    customers = db.query(Customer).intersect_all()
        
    # Always check if the customer exists before accessing relationships
    # This makes sure we don't run into AttributeError if the customer is not found    
    if customers: 
        for customer in customers:
            print(f"Customer: {customer.customerName}, City: {customer.city}")

def test_customer_cities(db: Session):
    customers = db.query(Customer).all()
    cities = set(customer.city for customer in customers if customer.city)
    print("Unique cities where customers are located:")
    if customers:
        for city in cities:
            print(city)

def get_cities_with_orders(db: Session):
    customers = db.query(Customer).filter(Customer.city.isnot(None)).all()
    cities_with_orders = DefaultDict(int)
    
    for customer in customers:
        if customer.orders:
            cities_with_orders[customer.city] += len(customer.orders)
    
    print("Cities with orders:")
    for city, count in cities_with_orders.items():
        print(f"{city}: {count} orders")

    print()
    print(sum(cities_with_orders.values()), "total orders across all cities")
    
def get_orders(db: Session):
    orders = db.query(Order).all()
    orderNumbers = set(order.orderNumber for order in orders)
    print(len(orderNumbers), "unique order numbers")
    
        
    



if __name__ == "__main__":
    db = get_db_connection("ordertracking")
    
    try:
        get_cities_with_orders(db)
    except Exception as err:
        print(f"ERROR: {err}")
    finally:
        db.close()