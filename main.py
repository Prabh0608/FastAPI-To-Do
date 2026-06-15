from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import dataBase
from Route.taskRoutes import router
from Route.userRoutes import userRouter
from utils.AppError import AppError
from fastapi.responses import JSONResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    await dataBase()
    yield
    print("Application shutting down")

app = FastAPI(lifespan=lifespan)

app.include_router(router)
app.include_router(userRouter)

@app.exception_handler(AppError)
async def app_error_handler(request, exc: AppError):
    message = exc.message
    statusCode = exc.status_code

    return JSONResponse(
        status_code=statusCode,
        content={"status": "Failed", "error": message} 
    )

@app.exception_handler(Exception)
async def global_exception_handler(request, exc: Exception):
    print({str(exc)})
    
    return JSONResponse(
        status_code=500,
        content={"status": "Failed", "error": "Oopss!!! Something went wrong."}
    )