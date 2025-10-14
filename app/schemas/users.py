from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserOut(BaseModel):

    id: int
    name: str
    surname: str
    email: EmailStr
    is_superuser: bool

class UserCreate(BaseModel):
    name: str = Field(max_length=30)
    surname: Optional[str] = Field(default=None, max_length=30)
    email: EmailStr
    password: str
    
class UserCreateSuperUser(UserCreate):

    is_superuser: Optional[bool] = Field(default=True)

class UserUpdate(BaseModel):
    name: Optional[str] = Field(default=None, max_length=30)
    surname: Optional[str] = Field(default=None, max_length=30)
    email: Optional[EmailStr] = None

class UserUpdatePassword(BaseModel):
    password1: str
    password2: str
    new_password: str

class UserUpdateSuperUser(BaseModel):
    is_superuser: bool