from motor.motor_asyncio import AsyncIOMotorClient
from config import settings

db = settings.dataBaseUri
client = AsyncIOMotorClient(db)
database = client["Tasks"]
collection = database["Task"]
userDatabase = client["Users"]
userCollection = userDatabase["User"]
async def dataBase():
    try:
        await client.admin.command('ping')
        print('Connected with Database successfully!')
    except Exception as e:
        raise('Error while connecting your DB')