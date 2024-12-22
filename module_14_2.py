# Копируем код из предыдущего задания
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
    cursor.execute("INSERT INTO Users (id, username, email, age, balance) VALUES (?, ?, ?, ?, ?)",
                   (i+1, f"User{i+1}", f"example{i+1}@gmail.com", f"{i+1}0", "1000"))
    if i % 2 == 0:
        cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i+1}"))
    if i % 3 == 0:
        cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i+1}", ))

# Закомментируем блок вывода базы данных в консоль, поскольку это не требуется текущим заданием
# cursor.execute("SELECT id, username, email, age, balance FROM Users WHERE age > ?", (0, ))
# users = cursor.fetchall()
# for id, username, email, age, balance in users:
#     print(f'ID: {id} | Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

# Удаление пользователя с id=6
cursor.execute("DELETE FROM Users WHERE id = ?", (6, ))

# Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(total_users)

# Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances)

# Вывод на консоль
print(all_balances / total_users)

connection.commit()
connection.close()