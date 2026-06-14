import pymysql
import random

# List of PH locations (City, State/Province, PostalCode)
ph_locations = [
    ("Manila", "Metro Manila", "1000"),
    ("Quezon City", "Metro Manila", "1100"),
    ("Cebu City", "Cebu", "6000"),
    ("Davao City", "Davao del Sur", "8000"),
    ("Makati", "Metro Manila", "1200"),
    ("Baguio", "Benguet", "2600"),
    ("Iloilo City", "Iloilo", "5000"),
    ("Bacoor", "Cavite", "4102"),
    ("Cagayan de Oro", "Misamis Oriental", "9000"),
    ("Zamboanga City", "Zamboanga del Sur", "7000"),
    ("Taguig", "Metro Manila", "1630"),
    ("Pasig", "Metro Manila", "1600")
]

def update_customers_to_ph():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='ordertracking'
        )
        
        with connection.cursor() as cursor:
            # 1. Get all customer numbers
            cursor.execute("SELECT customerNumber FROM customers")
            customers = cursor.fetchall()
            
            print(f"Updating {len(customers)} customers to Philippines locations...")
            
            for (cust_num,) in customers:
                city, state, postal = random.choice(ph_locations)
                
                # Update the customer record
                sql = """
                    UPDATE customers 
                    SET city = %s, 
                        state = %s, 
                        country = 'Philippines', 
                        postalCode = %s,
                        addressLine1 = CONCAT(FLOOR(100 + RAND() * 900), ' Street Name')
                    WHERE customerNumber = %s
                """
                cursor.execute(sql, (city, state, postal, cust_num))
            
            connection.commit()
            print("Successfully updated all customers.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    update_customers_to_ph()
