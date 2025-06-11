from pydantic import BaseModel, Field
from typing import Optional

class TaskAttributes(BaseModel):
    title: str = Field(..., title="Título de la tarea", description="Lo que hay que hacer")
    description: Optional[str] = Field(default=None, title="Nota", description="Detalles u observaciones")
    done: Optional[bool] = Field(default=False)

class TaskDataCreate(BaseModel):
    type: str
    attributes: TaskAttributes

class TaskDataUpdate(BaseModel):
    type: str
    attributes: TaskAttributes

class TaskCreateRequest(BaseModel):
    data: TaskDataCreate

class TaskUpdateRequest(BaseModel):
    data: TaskDataUpdate

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskResponse(TaskBase):
    id: int
    done: bool

    class Config:
        orm_mode = True
