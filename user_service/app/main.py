import requests
from fastapi import FastAPI, HTTPException, status
from typing import List
from app.model.user import User, Gender, Role, UserUpdateRequest
from uuid import UUID

# uvicorn user_service.main:user_service --reload
app = FastAPI()

db: List[User] = [
    User(
        id=UUID('86f053a0-0dd1-4439-ba43-bdf586220bd2'),
        first_name='Aboba',
        last_name="Ivanov",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID('1f4ee684-6856-4a17-8ff2-e0492d3c9099'),
        first_name='Alex',
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.teacher]
    ),
    User(
        id=UUID('e1161271-c9d1-47b3-95d1-d879bd137a2a'),
        first_name='Test',
        last_name="Test",
        gender=Gender.male,
        roles=[Role.admin]
    )
]

@app.get("/health", status_code=status.HTTP_200_OK)
async def user_health():
    return {'message': 'service is active'}

@app.get("/users")
async def fetch_users():
    return db


@app.get("/user_data/{user_id}")
async def fetch_users(user_id: UUID):

    r = requests.get(f"http://documents_service/doc_by_id/{user_id}")
    r_dict = r.json()
    u: User
    for user in db:
        if user.id == user_id:
            u = user
            return {
                'user': u.as_dict(),
                'document': r_dict
            }
    raise HTTPException(
        status_code=404,
        detail=f'user with {user_id} does not exist'
    )

@app.post("/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f'user with {user_id} does not exist'
    )

@app.put("/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.gender is not None:
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f'user with {user_id} does not exist'
    )
