
from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Role, User, UpdateUser
from uuid import UUID
from fastapi import HTTPException

app = FastAPI()

db: List[User] = [
    User(
    id=uuid4(),
    first_name="John",
    last_name="Doe",
    age = "15",
    gender=Gender.male,
    roles=[Role.user],
    ),
    User(
    id=uuid4(),
    first_name="Jane",
    last_name="Doe",
    age = "23", 
    gender=Gender.female,
    roles=[Role.user],
    ),
    User(
    id=uuid4(),
    first_name="James",
    last_name="Gabriel",
    age = "13",
    gender=Gender.male,
    roles=[Role.user],
    ),
]

@app.get("/") # 初期画面
async def root():
    return {"Hello": "World",}

@app.get("/api/v1/users") # ユーザの一覧を取得
async def get_users():
    return db

@app.post("/api/v1/users") # 新規ユーザの作成
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{id}") # ユーザの削除
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(status_code=404, detail=f"Delete user failed, id {id} not found.")

@app.put("/api/v1/users/{id}") # ユーザ情報の更新
async def update_user(user_update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.age is not None:
                user.age = user_update.age
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user.id
        raise HTTPException(status_code=404, detail=f"Delete user failed, id {id} not found.")