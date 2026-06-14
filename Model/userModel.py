from pydantic import BaseModel, EmailStr, SecretStr, Field, model_validator
from datetime import datetime
from typing_extensions import Self

class userCreate(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50,
        strip_whitespace=True
    )
    email: EmailStr
    password: SecretStr = Field(min_length=8)
    confirmPassword: SecretStr

    @model_validator(mode='after')
    def passwordVerify(self) -> Self:
        if self.password.get_secret_value() != self.confirmPassword.get_secret_value():
             raise ValueError("Passwords do not match")
        return self

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