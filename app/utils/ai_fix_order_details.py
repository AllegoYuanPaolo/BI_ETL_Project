import pymysql
import random

def fix_order_details():
    try:
        connection = pymysql.connect(host='localhost', user='root', password='', database='ordertracking')
        with connection.cursor() as cursor:
            # 1. Fetch valid product codes
            cursor.execute("SELECT productCode, MSRP FROM products")
            all_products = cursor.fetchall()
            
            if not all_products:
                print("Error: No products found in database.")
                return

            # 2. Target orders ORD015 to ORD054
            order_numbers = [f"ORD{i:03d}" for i in range(15, 55)]
            
            for order_num in order_numbers:
                # Check if order exists and if it already has details
                cursor.execute("SELECT count(*) FROM orderdetails WHERE orderNumber = %s", (order_num,))
                if cursor.fetchone()[0] > 0:
                    print(f"Skipping {order_num}: Already has details.")
                    continue
                
                cursor.execute("SELECT count(*) FROM orders WHERE orderNumber = %s", (order_num,))
                if cursor.fetchone()[0] == 0:
                    print(f"Skipping {order_num}: Order record does not exist.")
                    continue

                print(f"Generating details for {order_num}...")
                
                # Generate 1-5 order details
                num_items = random.randint(1, 5)
                order_total = 0
                selected_products = random.sample(all_products, num_items)
                
                for line_num, (prod_code, msrp) in enumerate(selected_products, 1):
                    qty = random.randint(1, 50)
                    price = float(msrp) * random.uniform(0.8, 1.1)
                    item_total = qty * price
                    order_total += item_total
                    
                    cursor.execute("""
                        INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (order_num, prod_code, qty, price, line_num))
                
                # Update the order total to match the details
                cursor.execute("UPDATE orders SET total_Price = %s WHERE orderNumber = %s", (order_total, order_num))

            connection.commit()
            print("Finished fixing order details.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    fix_order_details()
