from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.services.user_service import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def authenticate_user(username: str, password: str, user_service: UserService):
    user = user_service.get_user_by_username(username)
    if not user or not user.check_password(password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return user


def create_access_token(data: dict, secret: str, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret, algorithm="HS256")
    return encoded_jwt


def get_current_user(token: str, secret: str, user_service: UserService):
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=400, detail="Invalid JWT")
        user = user_service.get_user_by_username(username=username)
        if user is None:
            raise HTTPException(status_code=400, detail="User not found")
        return user
    except jwt.PyJWTError:
        raise HTTPException(status_code=400, detail="Could not validate credentials")


async def setup_security(app):
    app.dependency_overrides[UserService] = UserService()
    app.dependency_overrides[get_current_user] = get_current_user
