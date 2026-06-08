from pydantic import BaseModel

class taskModel(BaseModel):
    title: str
    description: str
    status: bool

class resTaskModel(BaseModel):
    id: str
    title: str
    description: str
    status: bool

class updateTask(BaseModel):
    title: str | None = None
    description: str | None = None
    status: bool | None = None