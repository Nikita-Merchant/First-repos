import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance TEXT NOT NULL)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_username ON Users(username)")

for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i+1}", f"example{i+1}@gmail.com", f"{i+1}0", "1000"))
    if i % 2 == 0:
        cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i+1}"))
    if i % 3 == 0:
        cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i+1}", ))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60, ))
users = cursor.fetchall()
for username, email, age, balance in users:
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

connection.commit()
connection.close()
