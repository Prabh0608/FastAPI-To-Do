from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import dataBase
from Route.taskRoutes import router
# from Schema.taskSchema import task NOTE: 2nd way to perform REQ, RES

@asynccontextmanager
async def lifespan(app: FastAPI):
    await dataBase()
    yield
    print("Application shutting down")

app = FastAPI(lifespan=lifespan)

app.include_router(router)