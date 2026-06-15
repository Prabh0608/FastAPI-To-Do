from fastapi import APIRouter, Depends, Response
from Model.userModel import userResponse, userCreate
from Controller.userController import createUser, loginUser
from fastapi.security import OAuth2PasswordRequestForm

userRouter = APIRouter()

@userRouter.post('/register', response_model=userResponse)
async def create_user(userCreate: userCreate):
    return await createUser(userCreate) 

@userRouter.post('/logIn')
async def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    return await loginUser(form_data, response)