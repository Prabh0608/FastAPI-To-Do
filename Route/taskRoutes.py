from bson import ObjectId
from fastapi import status, APIRouter, Depends
from database import collection
from Model.taskModel import resTaskModel, taskModel, updateTask
from Controller import taskController
from utils.security import protect

router = APIRouter()

@router.get('/task/{taskID}', response_model= resTaskModel, status_code=status.HTTP_200_OK)
async def get_task_id(taskID: str, current_user: dict = Depends(protect)):
    return await taskController.getTaskByID(taskID, current_user=current_user)

@router.post('/task', status_code=status.HTTP_201_CREATED)
async def create_task(taskModel: taskModel, current_user: dict = Depends(protect)):
    return await taskController.createTask(taskModel, current_user=current_user)

@router.get('/task', response_model=list[resTaskModel])
async def get_all_task(current_user: dict = Depends(protect)):
    return await taskController.getAllTask(current_user=current_user)

@router.patch('/task/{taskID}', response_model= resTaskModel, status_code=status.HTTP_200_OK)
async def update_task(taskID: str, updateModel: updateTask, current_user: dict = Depends(protect)):
    return await taskController.updateTask(taskID, updateModel,current_user=current_user)
    
@router.delete('/task/{taskID}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(taskID: str, current_user: dict = Depends(protect)):
    return await taskController.deleteTask(taskID,current_user=current_user)