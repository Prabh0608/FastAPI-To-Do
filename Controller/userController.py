import bcrypt
from database import userCollection
import jwt
from config import settings
from utils.AppError import AppError
import time

def createJWT(user, response, msg):
    token = jwt.encode({"sub": str(user["_id"]), "exp": int(time.time()) + 1800}, settings.jwt_key, settings.jwt_algo)
    response.set_cookie(key="JWT", value=token, httponly=True, secure=True)
    return {"status": "Success", "message": msg}

async def createUser(userCreate, response):
    password = userCreate.password.get_secret_value()
    email = userCreate.email
    existing_user = await userCollection.find_one({"email": email})
    
    if existing_user:
        raise AppError(message="Email already exists", status_code=400)
    
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)

    userDict = userCreate.model_dump()
    userDict.pop("password", None)
    userDict.pop("confirmPassword", None)

    userDict["hashed_password"] = hashed_password

    await userCollection.insert_one(userDict)

    return createJWT(userDict, response, "Successfully registered!")

async def loginUser(formData, response):
    email = formData.username
    password = formData.password.encode('utf-8')
    user = await userCollection.find_one({"email": email})
    if user:
        if bcrypt.checkpw(password, user["hashed_password"]):
            return createJWT(user, response,  "Successfully Logged In!")
        
    raise AppError(message="Incorrect email or password", status_code=401)