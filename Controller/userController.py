import bcrypt
from database import userCollection

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