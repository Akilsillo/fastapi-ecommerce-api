from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.users import User
from app.schemas.users import UserCreate, UserUpdate, UserOut

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate):
        db_user = User(**user.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int):
        return self.db.scalar(select(User).where(User.user_id == user_id))

    def get_user_by_email(self, email: str):
        return self.db.scalar(select(User).where(User.email == email))

    def get_all_users(self):
        return self.db.scalars(select(User)).all()

    def update_user(self, user_id: int, user_update: UserUpdate):
        db_user = self.get_user(user_id)
        if db_user:
            for key, value in user_update.model_dump(exclude_unset=True).items():
                setattr(db_user, key, value)
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        db_user = self.get_user(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
        return db_user