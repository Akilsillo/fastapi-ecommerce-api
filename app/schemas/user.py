from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserOut(BaseModel):

    id: int
    name: str
    surname: str
    email: EmailStr
    is_superuser: bool
    

class UserCreate(BaseModel):

    name: str
    surname: Optional[str]
    email: EmailStr
    password: str
    
class UserCreateSuperUser(UserCreate):

    is_superuser: Optional[bool] = Field(default=True)


class UserUpdatePassword(BaseModel):
    
    id: int
    password1: str
    password2: str
    new_password: str