from pydantic import BaseModel, EmailStr, SecretStr, Field
from datetime import datetime

class userCreate(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50,
        strip_whitespace=True
    )
    email: EmailStr
    password: SecretStr = Field(min_length=8)
    confirmPassword: SecretStr

class userResponse(BaseModel):
    id: str
    name: str
    email: EmailStr

class userInDB(BaseModel):
    id: str
    name: str
    email: EmailStr
    hashed_password: str
    created_at: datetime 