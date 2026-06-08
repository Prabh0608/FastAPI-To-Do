from motor.motor_asyncio import AsyncIOMotorClient
from config import settings

db = settings.dataBaseUri
client = AsyncIOMotorClient(db)
database = client["Tasks"]
collection = database["Task"]
async def dataBase():
    try:
        await client.admin.command('ping')
        print('Connected with Database successfully!')
    except Exception as e:
        print('Error while connecting your DB')