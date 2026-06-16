from fastapi import Cookie
from config import settings
from database import userCollection
from utils.AppError import AppError
from bson import ObjectId
import jwt

async def protect(JWT: str = Cookie(None)):
    if not JWT:
        raise AppError(message="You are not logged in! Please log in to get Access.", status_code=401)
    try:
        payload = jwt.decode(JWT, settings.jwt_key, settings.jwt_algo)
        id = payload.get("sub")
        user = await userCollection.find_one({"_id": ObjectId(id)})
        return user
    except:
        raise AppError('The cookie is either expired or invalid', status_code=401)
        