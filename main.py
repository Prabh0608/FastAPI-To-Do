from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import dataBase
from Route.taskRoutes import router
from Route.userRoutes import userRouter

@asynccontextmanager
async def lifespan(app: FastAPI):
    await dataBase()
    yield
    print("Application shutting down")

app = FastAPI(lifespan=lifespan)

app.include_router(router)
app.include_router(userRouter)
