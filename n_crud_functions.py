# Скачиваем код из предыдущего задания
import sqlite3

connection = sqlite3.connect('products_for_telegram.db')
cursor = connection.cursor()

# Дополняем функцию для создания базы данных Users
def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    ''')
    connection.commit()

def get_all_products():
    connection = sqlite3.connect('products_for_telegram.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    prod_list = cursor.fetchall()
    connection.commit()
    return prod_list

# Пишем функцию для дополнения базы данных новым юзером
def add_user(username, email, age):
    connection = sqlite3.connect('products_for_telegram.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)", (username, email, age, 1000))
    connection.commit()

# Пишем функцию для определения наличия в базе данных юзера
def is_included(username):
    connection = sqlite3.connect('products_for_telegram.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users WHERE username = ?", (username, ))
    result = cursor.fetchone()
    connection.commit()
    if result:
        return True
    else:
        return False

def create_nomenkl():
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)",
                       (i, f"Product_{i}", f"описание {i}", i * 100))
    connection.commit()

initiate_db()
connection.commit()
connection.close()