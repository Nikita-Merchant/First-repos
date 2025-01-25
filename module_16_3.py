from fastapi import FastAPI, Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Создаем словарь для работы приложения
users = {'1': 'Имя: Example, возраст: 18'}

# Определение маршрута гет-запроса к словарю
@app.get("/users")
async def get_dict_page():
    return users

# Определение маршрута пост-запроса
@app.post("/user/{username}/{age}")
async def post_page(username: Annotated[str, Path(min_length=1, max_length=100, description='Enter username', example='Vasilij')],
                              age: Annotated[int, Path(ge=1, le=120, description='Enter age', example=17)]):
    new_id = max(int(key) for key in users.keys()) + 1
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f"User {new_id} is registered"

# Определение маршрута пут-запроса
@app.put("/user/{user_id}/{username}/{age}")
async def update_page(user_id: Annotated[int, Path(ge=0, le=12000, description='Enter id', example=24)],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                       age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is updated"

# Определение маршрута делит-запроса
@app.delete("/user/{user_id}")
async def delete_page(user_id: Annotated[int, Path(ge=0, le=12000, description='Enter id', example=24)]):
    del_id = users.pop(user_id, 'flag')
    if del_id == 'flag':
        return f"The user {user_id} is not found"
    else:
        return f'The user {user_id} is deleted'