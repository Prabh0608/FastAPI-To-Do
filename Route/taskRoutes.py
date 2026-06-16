from bson import ObjectId
from fastapi import status, APIRouter, Depends
from database import collection
from Model.taskModel import resTaskModel, taskModel, updateTask
from Controller import taskController
from utils.security import protect

router = APIRouter(dependencies=[Depends(protect)])

@router.get('/task/{taskID}', response_model= resTaskModel, status_code=status.HTTP_200_OK)
async def get_task_id(taskID: str):
    return await taskController.getTaskByID(taskID)

@router.post('/task', status_code=status.HTTP_201_CREATED)
async def create_task(taskModel: taskModel):
    return await taskController.createTask(taskModel)

@router.get('/task', response_model=list[resTaskModel], status_code=status.HTTP_200_OK)
async def get_all_task():
    return await taskController.getAllTask()

@router.patch('/task/{taskID}', response_model= resTaskModel, status_code=status.HTTP_200_OK)
async def update_task(taskID: str, updateModel: updateTask):
    return await taskController.updateTask(taskID, updateModel)
    
@router.delete('/task/{taskID}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(taskID: str):
    return await taskController.deleteTask(taskID)