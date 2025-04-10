import csv
import uuid
from datetime import datetime, timedelta
import random

# Valores preestablecidos para set_num
set_num_values = [
    "0015-1", "010-1", "045-1", "065-1", "0906946506-1", "1000565897-5", "10019-1",
    "10041-1", "10059-1", "101032405-1", "10133-1", "10173-1", "102-1", "10240-1",
    "10292-1", "10391-1", "10511-1", "10572-1", "1062-1", "10701-1", "21000-1",
    "2101259516196-1", "21-1", "211901-1", "21344-1", "215-2B", "218158-1", "226-4",
    "242.1-1", "271723-1", "41801-1", "41944-1", "5007392-1", "5007613-1", "5007877-1",
    "5008162-1", "5009187-1", "702-1", "7042-1", "70706-1", "7511-1", "852545-1", "951178-1"
]



# Función para generar datos de la tabla 'sets'
def generate_sets():
    sets = []
    for set_num in set_num_values:
        name = f"Set Name {set_num}"
        year = random.randint(2000, 2023)
        theme_id = f"THEME-{random.randint(1, 10)}"
        num_parts = random.randint(50, 1000)
        img_url = f"https://example.com/sets/{set_num}.jpg"
        sets.append([set_num, name, year, theme_id, num_parts, img_url])
    return sets

# Función para generar datos de la tabla 'users'
def generate_users(num_records):
    users = []
    for i in range(num_records):
        user_id = f"USER-{uuid.uuid4().hex[:6].upper()}"
        username = f"user{i+1}"
        email = f"{username}@example.com"
        users.append([user_id, username, email])
    return users

# Función para generar datos de la tabla 'orders'
def generate_orders(num_records, users):
    orders = []
    for i in range(num_records):
        order_id = f"ORDER-{uuid.uuid4().hex[:6].upper()}"
        user_id = random.choice(users)[0]  # Selecciona un user_id aleatorio
        total_amount = round(random.uniform(10.0, 500.0), 2)
        orders.append([order_id, user_id, total_amount])
    return orders

# Función para generar datos de la tabla 'order_details'
def generate_order_details(num_records, orders, sets):
    order_details = []
    start_date = datetime(2024, 1, 1)
    end_date = datetime.now()
    for i in range(num_records):
        order_detail_id = f"DETAIL-{uuid.uuid4().hex[:6].upper()}"
        order_id = random.choice(orders)[0]  # Selecciona un order_id aleatorio
        set_num = random.choice(sets)[0]  # Selecciona un set_num de la lista preestablecida
        quantity = random.randint(1, 10)
        price = round(random.uniform(5.0, 100.0), 2)
        

        random_days = random.randint(0, (end_date - start_date).days)
        order_date = start_date + timedelta(days=random_days)
        order_date_str = order_date.strftime("%Y-%m-%d")

        order_details.append([order_detail_id, order_id, set_num, quantity, price, order_date_str])


    return order_details

# Función para generar datos de la tabla 'shipments'
def generate_shipments(num_records, orders):
    shipments = []
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    countries = ["USA", "Canada", "Mexico"]
    for i in range(num_records):
        ship_id = f"SHIP-{uuid.uuid4().hex[:6].upper()}"
        order_id = random.choice(orders)[0]  # Selecciona un order_id aleatorio
        city_ship = random.choice(cities)
        country_ship = random.choice(countries)
        shipments.append([ship_id, order_id, city_ship, country_ship])
    return shipments

# Función para generar datos de la tabla 'reviews'
def generate_reviews(num_records, users, sets):
    reviews = []
    for i in range(num_records):
        review_id = f"REVIEW-{uuid.uuid4().hex[:6].upper()}"
        user_id = random.choice(users)[0]  # Selecciona un user_id aleatorio
        set_num = random.choice(sets)[0]  # Selecciona un set_num de la lista preestablecida
        rating = random.randint(1, 5)
        reviews.append([review_id, user_id, set_num, rating])
    return reviews

# Función para guardar datos en un archivo CSV
def save_to_csv(filename, headers, data):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


num_records = 1000  # Número de registros por tabla

sets_data = generate_sets()
users_data = generate_users(num_records)
orders_data = generate_orders(num_records, users_data)
order_details_data = generate_order_details(num_records, orders_data, sets_data)
shipments_data = generate_shipments(num_records, orders_data)
reviews_data = generate_reviews(num_records, users_data, sets_data)

# Guardar datos en archivos CSV
save_to_csv("sets.csv", ["set_num", "name", "year", "theme_id", "num_parts", "img_url"], sets_data)
save_to_csv("users.csv", ["user_id", "username", "email"], users_data)
save_to_csv("orders.csv", ["order_id", "user_id", "total_amount"], orders_data)
save_to_csv("order_details.csv", ["order_detail_id", "order_id", "set_num", "quantity", "price","order_date"], order_details_data)
save_to_csv("shipments.csv", ["ship_id", "order_id", "city_ship", "country_ship"], shipments_data)
save_to_csv("reviews.csv", ["review_id", "user_id", "set_num", "rating"], reviews_data)

print("Archivos CSV generados.")
