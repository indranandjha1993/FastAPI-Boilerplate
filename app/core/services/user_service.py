from typing import List

from app.core.models.user import User
from app.database.base import Base


class UserService:
    def __init__(self, database: Base):
        self.database = database

    def get_all_users(self) -> List[User]:
        session = self.database.session()
        users = session.query(User).all()
        session.close()

        return users

    def get_user_by_username(self, username: str) -> User:
        session = self.database.session()
        user = session.query(User).filter_by(username=username).first()
        session.close()

        return user

    def add_user(self, user: User):
        session = self.database.session()
        session.add(user)
        session.commit()
        session.close()

    def delete_user(self, user: User):
        session = self.database.session()
        session.delete(user)
        session.commit()
        session.close()

    def get_user_by_id(self, user_id):
        session = self.database.session()
        user = session.query(User).filter_by(id=user_id).first()
        session.close()

        return user

