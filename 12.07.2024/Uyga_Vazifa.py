# # import requests
# # import json
# # import threading
# # import psycopg2
# #
# #
# # conn = psycopg2.connect(host="localhost", dbname="homeworks", user="postgres", password="1234", port="5432")
# # cursor = conn.cursor()
# #
# # user_url = requests.get('https://dummyjson.com/users')
# #
# # user_list = user_url.json()['users']
# #
# # # print(user_list)
# #
# # # create_query = """
# # # CREATE TABLE IF NOT EXISTS users (
# # #         id SERIAL PRIMARY KEY,
# # #         first_name VARCHAR(100) NOT NULL,
# # #         last_name VARCHAR(100) NOT NULL,
# # #         maidenName VARCHAR(100) NOT NULL,
# # #         age INTEGER NOT NULL,
# # #         gender VARCHAR(100) NOT NULL,
# # #         email VARCHAR(100)NOT NULL,
# # #         phone VARCHAR(100)NOT NULL,
# # #         username VARCHAR(100) NOT NULL,
# # #         password VARCHAR(100) NOT NULL,
# # #         birth_date VARCHAR(100) NOT NULL,
# # #         image_url VARCHAR(100) NOT NULL,
# # #         blood_type VARCHAR(100) NOT NULL,
# # #         height INTEGER NOT NULL,
# # #         weight INTEGER NOT NULL,
# # #         eye_color VARCHAR(100) NOT NULL,
# # #         hair_color VARCHAR(100) NOT NULL,
# # #         hair_type VARCHAR(100) NOT NULL,
# # #         ip_address VARCHAR(100) NOT NULL,
# # #         address VARCHAR(100) NOT NULL,
# # #         city VARCHAR(100) NOT NULL,
# # #         state VARCHAR(100) NOT NULL,
# # #         state_code VARCHAR(100) NOT NULL,
# # #         postal_code VARCHAR(100) NOT NULL,
# # #         coordinates VARCHAR(100) NOT NULL)
# # #
# # # """
# # # conn.cursor().execute(create_query)
# # # conn.commit()
# #
# #
# # # select = """Select * from users"""
# # # cur = conn.cursor()
# # # cur.execute(select)
# # # users = cur.fetchall()
# # # for user in users:
# # #     print(user)
# # #
# # insert = """Insert into users (username, email, password) values(12, 771, 1234)
# # """
# # cur = conn.cursor()
# # cur.execute(insert)
# # conn.commit()
# # # def download_file(url, filename):
# # #     response = requests.get(url)
# # #     with open(filename, 'w') as f:
# # #         json.dump(response.json(), f, indent=4)
# # #         print(response.status_code)
# # #
# # #
# # #
# # #     urls = [
# # #         ('https://dummyjson.com/products', 'products.json'),
# # #         ('https://dummyjson.com/users', 'users.json')
# # #     ]
# # #
# # #     threads = [
# # #         threading.Thread(target=download_file, args=(url, filename))
# # #         for url, filename in urls]
# # #
# # #     for thread in threads:
# # #         thread.start()
# # #
# # #     for thread in threads:
# # #         thread.join()
# # #
# # # if __name__ == '__main__':
# # #     pass
# # # import requests
# # # import psycopg2
# # #
# # # # URL JSON-файла
# # # json_url = "https://dummyjson.com/users"
# # #
# # # # Параметры подключения к базе данных
# # # db_params = {
# # #     "dbname": "homeworks",
# # #     "user": "postgres",
# # #     "password": "1234",
# # #     "host": "localhost",
# # #     "port": "5432"
# # # }
# # #
# # # # Загрузка JSON-файла по URL
# # # response = requests.get(json_url)
# # # data_dict = response.json()
# # #
# # # # Подключение к базе данных
# # # conn = psycopg2.connect(**db_params)
# # # cursor = conn.cursor()
# # #
# # # # Создание таблицы users (пример для структуры данных users)
# # # query = ("""
# # #     CREATE TABLE IF NOT EXISTS users (
# # #         id SERIAL PRIMARY KEY,
# # #         first_name VARCHAR(100) NOT NULL,
# # #         last_name VARCHAR(100) NOT NULL,
# # #         maidenName VARCHAR(100) NOT NULL,
# # #         age INTEGER NOT NULL,
# # #         gender VARCHAR(100) NOT NULL,
# # #         email VARCHAR(100)NOT NULL,
# # #         phone VARCHAR(100)NOT NULL,
# # #         username VARCHAR(100) NOT NULL,
# # #         password VARCHAR(100) NOT NULL,
# # #         birth_date VARCHAR(100) NOT NULL,
# # #         image_url VARCHAR(100) NOT NULL,
# # #         blood_type VARCHAR(100) NOT NULL,
# # #         height INTEGER NOT NULL,
# # #         weight INTEGER NOT NULL,
# # #         eye_color VARCHAR(100) NOT NULL,
# # #         hair_color VARCHAR(100) NOT NULL,
# # #         hair_type VARCHAR(100) NOT NULL,
# # #         ip_address VARCHAR(100) NOT NULL,
# # #         address VARCHAR(100) NOT NULL,
# # #         city VARCHAR(100) NOT NULL,
# # #         state VARCHAR(100) NOT NULL,
# # #         state_code VARCHAR(100) NOT NULL,
# # #         postal_code VARCHAR(100) NOT NULL,
# # #         coordinates VARCHAR(100) NOT NULL)
# # #
# # #
# # # """)
# # # cursor.execute(query)
# # #
# # #
# # # # Вставка данных из JSON в таблицу
# # # for user in data_dict["users"]:
# # #     query_2 = ('''
# # #         INSERT INTO users (id, username, age) VALUES (%s, %s, %s)
# # #     ''', (user["id"], user["username"], user["age"]))
# # # cursor.execute(query_2)
# # # # Сохранение изменений и закрытие соединения
# # # conn.commit()
# # # cursor.close()
# # # conn.close()
#
# import requests
# import psycopg2
# import json
#
# # URL JSON-файла
# user_url = requests.get('https://dummyjson.com/users')
# user_list = user_url.json()['users']
# print(user_list)
#
#
#
#
# # Параметры подключения к базе данных
# db_params = {
#     "dbname": "your_dbname",
#     "user": "your_username",
#     "password": "your_password",
#     "host": "your_host",
#     "port": "your_port"
# }
#
#
# response = requests.get(user_list[0]['url'], params=db_params)
# data_dict = response.json()
#
# # Подключение к базе данных
# conn = psycopg2.connect(
#     dbname=db_params["dbname"],
#     user=db_params["user"],
#     password=db_params["password"],
#     host=db_params["host"],
#     port=db_params["port"]
# )
# cursor = conn.cursor()
#
#
# query = """
#     CREATE TABLE IF NOT EXISTS users (
#         id SERIAL PRIMARY KEY,
#         first_name VARCHAR(100) NOT NULL,
#         last_name VARCHAR(100) NOT NULL,
#         maidenName VARCHAR(100) NOT NULL,
#         age INTEGER NOT NULL,
#         gender VARCHAR(100) NOT NULL,
#         email VARCHAR(100)NOT NULL,
#         phone VARCHAR(100)NOT NULL,
#         username VARCHAR(100) NOT NULL,
#         password VARCHAR(100) NOT NULL,
#         birth_date VARCHAR(100) NOT NULL,
#         image_url VARCHAR(100) NOT NULL,
#         blood_type VARCHAR(100) NOT NULL,
#         height INTEGER NOT NULL,
#         weight INTEGER NOT NULL,
# """
# insert = """INSERT INTO users (
#             id, first_name, last_name, maiden_name, age, gender, email, phone, username, password, birth_date, image_url, blood_type, height, weight
#         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """
# # cursor.execute(query)
# # conn.commit()


import requests
import psycopg2
import json

user_url = "https://dummyjson.com/users"

db_params = {
    "dbname": "homeworks",
    "user": "postgres",
    "password": "1234",
    "host": "localhost",
    "port": "5432"
}

response = requests.get(user_url, params=db_params)
data_dict = response.json()

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        maidenName VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL,
        gender VARCHAR(100) NOT NULL,
        email VARCHAR(100)NOT NULL,
        phone VARCHAR(100)NOT NULL,
        username VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        birth_date VARCHAR(100) NOT NULL,
        image_url VARCHAR(100) NOT NULL,
        blood_type VARCHAR(100) NOT NULL,
        height INTEGER NOT NULL,
        weight INTEGER NOT NULL,
    )
""")

for user in data_dict["users"]:
    cursor.execute('''
        INSERT INTO users (first_name,last_name,maidenName,age,gender,email,phone,username,password,birth_date,image_url,blood_type,height,weight) VALUES (%s, %s, %s)
    ''', (user["id"], user["first_name"], user["maidenName"],user["age"],user["gender"],user["email"],user["phone"],user["username"],user["password"],user["birth_date"],user["image_url"],user["image_url"],user["image_url"]))

conn.commit()
cursor.close()
conn.close()

