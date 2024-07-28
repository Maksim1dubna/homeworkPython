#Для запуска python -m uvicorn main:app
# Swagger /docs
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def main_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_page(user_id):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
async def user_age_page(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
    #http://127.0.0.1:8000/user?username=user&age=25



