from fastapi import FastAPI, Depends, HTTPException

from app.api.security import authenticate_user, create_access_token, get_current_user
from app.core.models.user import User
from app.core.services.user_service import UserService

app = FastAPI()


@app.post("/login")
async def login(user_service: UserService, username: str, password: str):
    user = authenticate_user(username, password, user_service)
    access_token = create_access_token({"sub": user.username}, "secret")
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/me")
async def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user


@app.get("/users/{user_id}")
async def read_user(user_id: int, user_service: UserService):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users")
async def create_user(user_service: UserService, user: User):
    user = user_service.add_user(user)
    return user
