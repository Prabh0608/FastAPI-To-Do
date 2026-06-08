from bson import ObjectId
from fastapi import status, APIRouter
from database import collection
from Model.taskModel import resTaskModel, taskModel, updateTask
from Controller import taskController

router = APIRouter()

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
async def deleteTask(taskID):
    await collection.find_one_and_delete({"_id": ObjectId(taskID)})
    return