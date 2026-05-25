import pymysql
import random

# Lists for realistic PH address generation
ph_cities = [
    ("Manila", "Metro Manila", "1000"), ("Quezon City", "Metro Manila", "1100"),
    ("Cebu City", "Cebu", "6000"), ("Davao City", "Davao del Sur", "8000"),
    ("Makati", "Metro Manila", "1200"), ("Baguio", "Benguet", "2600"),
    ("Iloilo City", "Iloilo", "5000"), ("Bacoor", "Cavite", "4102"),
    ("Cagayan de Oro", "Misamis Oriental", "9000"), ("Taguig", "Metro Manila", "1630"),
    ("Pasig", "Metro Manila", "1600"), ("Paranaque", "Metro Manila", "1700")
]

street_names = ["Rizal St.", "Mabini St.", "Quezon Ave.", "Ayala Ave.", "EDSA", "Bonifacio St.", "Luna St.", "España Blvd.", "Katipunan Ave.", "Shaw Blvd."]
barangays = ["Brgy. San Jose", "Brgy. Poblacion", "Brgy. Bagong Pag-asa", "Brgy. Bel-Air", "Brgy. Loyola Heights", "Brgy. Ugong"]

def generate_address():
    num = random.randint(1, 999)
    street = random.choice(street_names)
    brgy = random.choice(barangays)
    return f"{num} {street}, {brgy}"

def populate_data():
    try:
        connection = pymysql.connect(host='localhost', user='root', password='', database='ordertracking')
        with connection.cursor() as cursor:
            # 1. Clear and Update existing 4 customers
            print("Updating existing customers...")
            cursor.execute("SELECT customerNumber FROM customers")
            existing = cursor.fetchall()
            for (cust_num,) in existing:
                city, state, postal = random.choice(ph_cities)
                cursor.execute("""
                    UPDATE customers 
                    SET city=%s, state=%s, country='Philippines', postalCode=%s, addressLine1=%s
                    WHERE customerNumber=%s
                """, (city, state, postal, generate_address(), cust_num))

            # 2. Add 20 more customers
            print("Adding 20 more customers...")
            for i in range(5, 25):
                cust_num = f"CUST{i:03d}"
                city, state, postal = random.choice(ph_cities)
                cursor.execute("""
                    INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, state, postalCode, country, creditLimit)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'Philippines', %s)
                """, (cust_num, f"Customer {i}", "Dela Cruz", "Juan", "0917-000-0000", generate_address(), city, state, postal, random.randint(50000, 200000)))

            # 3. Add 40 more orders and their details
            print("Adding 40 more orders and their details...")
            cursor.execute("SELECT customerNumber FROM customers")
            all_cust = [c[0] for c in cursor.fetchall()]
            
            cursor.execute("SELECT productCode, MSRP FROM products")
            all_products = cursor.fetchall()
            
            if not all_products:
                print("Error: No products found in database. Cannot create order details.")
                return

            for i in range(15, 55):
                order_num = f"ORD{i:03d}"
                cust_num = random.choice(all_cust)
                
                # Insert order first (placeholder total_Price)
                cursor.execute("""
                    INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber, total_Price)
                    VALUES (%s, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 7 DAY), 'Shipped', %s, 0)
                """, (order_num, cust_num))

                # Generate 1-5 order details
                num_items = random.randint(1, 5)
                order_total = 0
                selected_products = random.sample(all_products, num_items)
                
                for line_num, (prod_code, msrp) in enumerate(selected_products, 1):
                    qty = random.randint(1, 50)
                    price = float(msrp) * random.uniform(0.8, 1.1) # Price varies slightly from MSRP
                    item_total = qty * price
                    order_total += item_total
                    
                    cursor.execute("""
                        INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (order_num, prod_code, qty, price, line_num))
                
                # Update the order total to match the details
                cursor.execute("UPDATE orders SET total_Price = %s WHERE orderNumber = %s", (order_total, order_num))

            connection.commit()
            print("Data expansion (including order details) complete.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    populate_data()
