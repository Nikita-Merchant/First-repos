from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Создаем класс для работы приложения
class User(BaseModel):
    id: int
    username: str
    age: int

# Создаем список для работы приложения
users = []

# Определение маршрута гет-запроса к списку
@app.get("/users")
async def get_dict_page() -> List[User]:
    return users

# Определение маршрута пост-запроса
@app.post("/user/{username}/{age}")
async def post_page(username: Annotated[str, Path(min_length=1, max_length=100, description='Enter username', example='Vasilij')],
                              age: Annotated[int, Path(ge=1, le=120, description='Enter age', example=17)]):
    user_id = len(users) + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user

# Определение маршрута пут-запроса
@app.put("/user/{user_id}/{username}/{age}")
async def update_page(user_id: Annotated[int, Path(ge=0, le=12000, description='Enter id', example=24)],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                       age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]):
    try:
        edit_user = [user for user in users if user.id == user_id][0]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

# Определение маршрута делит-запроса
@app.delete("/user/{user_id}")
async def delete_page(user_id: Annotated[int, Path(ge=0, le=12000, description='Enter id', example=24)]):
    try:
        del_user = [user for user in users if user.id == user_id][0]
        users.remove(del_user)
        return del_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')