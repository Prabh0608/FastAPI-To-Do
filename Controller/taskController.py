from bson import ObjectId
from database import collection
from fastapi import HTTPException, status

async def getTaskByID(taskID: str):
    try:
        fetchedTask = await collection.find_one({"_id": ObjectId(taskID)})
        if fetchedTask == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Task not found"
            )
        fetchedTask["id"] = str(fetchedTask["_id"])
        return fetchedTask
    except Exception as e:
        raise {
            "status": "error",
            "message": str(e)
        }

async def createTask(taskModel):
    pythonModel = taskModel.model_dump()
    newTask = await collection.insert_one(pythonModel)
    return {"status": "Success", "id": str(newTask.inserted_id) ,"Message": "Data inserted in database"}

async def getAllTask():
    tasks = await collection.find().to_list(length=None)
    for task in tasks:
        task["id"] = str(task["_id"])
    return tasks

async def updateTask(taskID, updateModel):
    pythonModel = updateModel.model_dump()
    task = await collection.find_one_and_update({"_id": ObjectId(taskID)}, {"$set": pythonModel}, return_document=True)
    task["id"] = str(task["_id"])
    return task