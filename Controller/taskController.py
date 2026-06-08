from bson import ObjectId
from database import collection
from fastapi import HTTPException, status

async def getTaskByID(taskID: str):
    fetchedTask = await collection.find_one({"_id": ObjectId(taskID)})
    if fetchedTask == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Task not found"
        )
    fetchedTask["id"] = str(fetchedTask["_id"])
    return fetchedTask

async def createTask(taskModel):
    try:
        pythonModel = taskModel.model_dump()
        newTask = await collection.insert_one(pythonModel)
        return {"status": "Success", "id": str(newTask.inserted_id) ,"Message": "Data inserted in database"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e) 
        )

async def getAllTask():
    try:
        tasks = await collection.find().to_list(length=None)
        for task in tasks:
            task["id"] = str(task["_id"])
        return tasks
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e) 
        )
    
async def updateTask(taskID, updateModel):
    try:
        pythonModel = updateModel.model_dump(exclude_unset=True)
        task = await collection.find_one_and_update({"_id": ObjectId(taskID)}, {"$set": pythonModel}, return_document=True)
        task["id"] = str(task["_id"])
        return task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e) 
        )