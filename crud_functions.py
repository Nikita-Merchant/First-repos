import sqlite3

connection = sqlite3.connect('products_for_telegram.db')
cursor = connection.cursor()

# Пишем функцию для создания базы данных Products
def initiate_db():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL)
''')
    connection.commit()

# Пишем функцию для извлечения данных из базы данных Products
def get_all_products():
    connection = sqlite3.connect('products_for_telegram.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    prod_list = cursor.fetchall()
    connection.commit()
    connection.close()
    return prod_list

# Пишем функцию для заполнения базы данных уместными записями
def create_nomenkl():
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)",
                       (i, f"Product_{i}", f"описание {i}", i * 100))
    connection.commit()

# Используя функции создаем и заполняем базу данных Products записями (после использования закомментировал блок)
# initiate_db()
# create_nomenkl()

connection.commit()
connection.close()