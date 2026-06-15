from bson import ObjectId
from database import collection
from fastapi import HTTPException, status
from utils.AppError import AppError

async def getTaskByID(taskID: str):
    fetchedTask = await collection.find_one({"_id": ObjectId(taskID)})
    if fetchedTask == None:
        raise AppError(message = "Task not found", status_code=404)
    fetchedTask["id"] = str(fetchedTask["_id"])
    return fetchedTask

async def createTask(taskModel):
    try:
        pythonModel = taskModel.model_dump()
        newTask = await collection.insert_one(pythonModel)
        return {"status": "Success", "id": str(newTask.inserted_id) ,"Message": "Data inserted in database"}
    except:
        raise AppError(message = "Error While Creating Task!", status_code=400)

async def getAllTask():
        tasks = await collection.find().to_list(length=None)
        if tasks == None:
            raise AppError(message = "Task not found", status_code=404)
        for task in tasks:
            task["id"] = str(task["_id"])
        return tasks
    
async def updateTask(taskID, updateModel):
        pythonModel = updateModel.model_dump(exclude_unset=True)
        task = await collection.find_one_and_update({"_id": ObjectId(taskID)}, {"$set": pythonModel}, return_document=True)
        if task == None:
            raise AppError(message = "Task not found", status_code=404)
        task["id"] = str(task["_id"])
        return task

async def deleteTask(taskID):
    deletedTask = await collection.find_one_and_delete({"_id": ObjectId(taskID)})
    if deletedTask == None:
            raise AppError(message = "Task not found", status_code=404)
    return