import pymysql
import random

# Realistic PH Business Types/Suffixes
business_types = [
    "Toy Emporium", "Collectibles", "Hobbies & More", "Diecast Hub", 
    "Toy Kingdom", "General Merchandise", "Miniature World", "Trading Post",
    "Hobby Shop", "Auto-Miniatures", "Retail Solutions", "Wholesale Center"
]

ph_locations = ["Manila", "Cebu", "Davao", "Makati", "Quezon City", "Pasig", "Baguio", "Iloilo", "Cavite", "Taguig"]

# Realistic PH Names for contacts
first_names = [
    "Juan", "Jose", "Maria", "Elena", "Ricardo", "Liza", "Antonio", "Carmen", 
    "Roberto", "Teresa", "Francisco", "Isabel", "Angel", "Dante", "Nenita",
    "Ramon", "Gloria", "Salvador", "Imelda", "Ferdinand", "Cory", "Benigno"
]

last_names = [
    "Dela Cruz", "Garcia", "Reyes", "Ramos", "Mendoza", "Santos", "Flores", 
    "Villanueva", "Bautista", "Castro", "Aquino", "Marcos", "Duterte", 
    "Robredo", "Pangilinan", "Go", "Poe", "Ejercito", "Sotto", "Lapid"
]

def generate_business_name():
    chance = random.random()
    if chance < 0.4:
        # e.g., "Manila Diecast Hub"
        return f"{random.choice(ph_locations)} {random.choice(business_types)}"
    elif chance < 0.7:
        # e.g., "Garcia's Collectibles"
        return f"{random.choice(last_names)}'s {random.choice(business_types)}"
    else:
        # e.g., "Metro Miniature World"
        prefix = random.choice(["Metro", "Grand", "Global", "Island", "Pearl"])
        return f"{prefix} {random.choice(business_types)}"

def generate_ph_phone():
    prefixes = ["0917", "0918", "0920", "0922", "0945", "0956", "0966", "0977"]
    main = "".join([str(random.randint(0, 9)) for _ in range(7)])
    return f"{random.choice(prefixes)}-{main[:3]}-{main[3:]}"

def update_customer_details():
    try:
        connection = pymysql.connect(host='localhost', user='root', password='', database='ordertracking')
        with connection.cursor() as cursor:
            cursor.execute("SELECT employeeNumber FROM employees")
            reps = [r[0] for r in cursor.fetchall()]
            
            cursor.execute("SELECT customerNumber FROM customers")
            customers = [c[0] for c in cursor.fetchall()]
            
            print(f"Updating business details for {len(customers)} customers...")
            
            for cust_num in customers:
                business_name = generate_business_name()
                contact_first = random.choice(first_names)
                contact_last = random.choice(last_names)
                phone = generate_ph_phone()
                rep = random.choice(reps)
                
                cursor.execute("""
                    UPDATE customers 
                    SET customerName = %s,
                        contactFirstName = %s,
                        contactLastName = %s,
                        phone = %s,
                        salesRepEmployeeNumber = %s
                    WHERE customerNumber = %s
                """, (business_name, contact_first, contact_last, phone, rep, cust_num))
            
            connection.commit()
            print("Successfully updated customer business names and contact info.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    update_customer_details()
