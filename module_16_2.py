from fastapi import FastAPI, Path
from typing import Annotated

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

# # Определение маршрута к айди пользователя с валидацией данных об Айди
@app.get("/user/{user_id}")
async def user_id_page(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=17)]):
    return f"Вы вошли как пользователь № {user_id}"

# # Определение маршрута к данным о пользователе с валидацией, указанных данных
@app.get("/user/{username}/{age}")
async def user_id_page(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                       age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"