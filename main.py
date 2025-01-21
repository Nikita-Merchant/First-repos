from fastapi import FastAPI

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def main_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

# Определение базового маршрута
@app.get("/user/{user_id}")
async def user_id_page(user_id: int = 1):
    return f"Вы вошли как пользователь № {user_id}"

# Определение базового маршрута
@app.get("/user")
async def user_id_page(username: str = 'Nick', age: int = 34):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"