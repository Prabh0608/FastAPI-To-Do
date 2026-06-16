from pydantic import BaseModel, EmailStr, SecretStr, Field, model_validator,field_validator
from typing_extensions import Self
from zxcvbn import zxcvbn

class userCreate(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50,
        strip_whitespace=True
    )
    email: EmailStr
    password: SecretStr = Field(min_length=8)
    confirmPassword: SecretStr

    @field_validator("password")
    @classmethod
    def strongPass(cls, value: SecretStr) -> SecretStr:
        rawPass = value.get_secret_value()
        results = zxcvbn(rawPass)
        if results["score"] < 2:
            feedback = results["feedback"]["warning"] or "Password is too guessable."
            raise ValueError(f"Weak password: {feedback}")  
        return value

    @model_validator(mode='after')
    def passwordVerify(self) -> Self:
        if self.password.get_secret_value() != self.confirmPassword.get_secret_value():
             raise ValueError("Passwords do not match")
        return self

class userResponse(BaseModel):
    id: str
    email: EmailStr