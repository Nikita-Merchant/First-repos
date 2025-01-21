from fastapi import FastAPI

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def main_page():
    return "Главная страница"

# Определение маршрута к странице админа
@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

# Определение маршрута к айди пользователя
@app.get("/user/{user_id}")
async def user_id_page(user_id: int = 1):
    return f"Вы вошли как пользователь № {user_id}"

# Определение маршрута к данным о пользователе
@app.get("/user")
async def user_id_page(username: str = 'Nick', age: int = 34):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"