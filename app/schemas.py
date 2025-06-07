from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    done: bool

class TaskResponse(TaskBase):
    id: int
    done: bool

    class Config:
        orm_mode = True