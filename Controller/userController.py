import bcrypt
from database import userCollection
from fastapi import HTTPException, status
import jwt
from config import settings


async def createUser(userCreate):
    password = userCreate.password.get_secret_value()
    
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)

    userDict = userCreate.model_dump()
    userDict.pop("password", None)
    userDict.pop("confirmPassword", None)

    userDict["hashed_password"] = hashed_password

    await userCollection.insert_one(userDict)

    userDict["id"] = str(userDict["_id"])

    return userDict

async def loginUser(formData, response):
    email = formData.username
    password = formData.password.encode('utf-8')
    user = await userCollection.find_one({"email": email})
    if user:
        if bcrypt.checkpw(password, user["hashed_password"]):
            token = jwt.encode({"sub": str(user["_id"])}, settings.jwt_key, "HS256")
            response.set_cookie(key="JWT", value=token, httponly=True, secure=True)
            return {"status": "Success", "message": "Cookie Created"}
        
    raise HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect email or password"
    )