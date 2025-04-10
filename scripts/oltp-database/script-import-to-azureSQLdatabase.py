import pyodbc
import pandas as pd


server = 'rebrickable-oltp.database.windows.net'
database = 'oltp_rebrickable'
username = 'nicolasgonzalez'
password = '' #aqui va la contraseña a utilizar
driver = '{ODBC Driver 17 for SQL Server}'


connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'


conn = pyodbc.connect(connection_string)
cursor = conn.cursor()


#users
csv_file_path = 'C:/Users/lenovo/Documents/VisualStudio/users.csv'
df = pd.read_csv(csv_file_path)
table_name = 'users'
for index, row in df.iterrows():
    query = f"INSERT INTO {table_name} (user_id, username, email) VALUES (?, ?, ?)"
    cursor.execute(query, row['user_id'],row['username'],row['email'])
conn.commit()

#orders
csv_file_path = 'C:/Users/lenovo/Documents/VisualStudio/orders.csv'
df = pd.read_csv(csv_file_path)
table_name = 'orders'
for index, row in df.iterrows():
    query = f"INSERT INTO {table_name} (order_id, user_id, total_amount) VALUES (?, ?, ?)"
    cursor.execute(query, row['order_id'],row['user_id'],row['total_amount'])
conn.commit()

#sets
 csv_file_path = 'C:/Users/lenovo/Documents/VisualStudio/sets.csv'
 df = pd.read_csv(csv_file_path)
 table_name = 'sets'
 for index, row in df.iterrows():
    query = f"INSERT INTO {table_name} (set_num, name, year, theme_id, num_parts, img_url) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(query, row['set_num'],row['name'],row['year'],row['theme_id'],row['num_parts'],row['img_url'])
conn.commit()

#order_details
csv_file_path = 'C:/Users/lenovo/Documents/VisualStudio/order_details.csv'
df = pd.read_csv(csv_file_path)
table_name = 'order_details'
for index, row in df.iterrows():
    query = f"INSERT INTO {table_name} (order_detail_id, order_id, set_num, quantity, price, order_date) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(query, row['order_detail_id'],row['order_id'],row['set_num'], row['quantity'], row['price'], row['order_date'])
conn.commit()

#shipments
csv_file_path = 'C:/Users/lenovo/Documents/VisualStudio/shipments.csv'
df = pd.read_csv(csv_file_path)
table_name = 'shipments'
for index, row in df.iterrows():
    query = f"INSERT INTO {table_name} (ship_id, order_id, city_ship, country_ship) VALUES (?, ?, ?, ?)"
    cursor.execute(query, row['ship_id'],row['order_id'],row['city_ship'],row['country_ship'])
conn.commit()

#reviews
csv_file_path = 'C:/Users/lenovo/Documents/VisualStudio/reviews.csv'
df = pd.read_csv(csv_file_path)
table_name = 'reviews'
for index, row in df.iterrows():
    query = f"INSERT INTO {table_name} (review_id, user_id, set_num, rating) VALUES (?, ?, ?, ?)"
    cursor.execute(query, row['review_id'],row['user_id'],row['set_num'],row['rating'])
conn.commit()




cursor.close()
conn.close()
