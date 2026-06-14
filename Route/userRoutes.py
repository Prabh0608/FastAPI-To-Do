from fastapi import APIRouter
from Model.userModel import userResponse, userCreate
from Controller.userController import createUser

userRouter = APIRouter()

@userRouter.post('/register', response_model=userResponse)
async def create_user(userCreate: userCreate):
    return await createUser(userCreate) 