from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks/", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_task(task_data: schemas.TaskCreateRequest, db: Session = Depends(get_db)):
    attributes = task_data.data.attributes
    db_task = models.Task(**attributes.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return {
        "data": {
            "type": "task",
            "id": db_task.id,
            "attributes": {
                "title": db_task.title,
                "description": db_task.description,
                "done": db_task.done
            }
        }
    }

@router.get("/tasks/", response_model=dict)
def read_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).filter(models.Task.is_deleted == False).all()
    return {
        "data": [
            {
                "type": "task",
                "id": task.id,
                "attributes": {
                    "title": task.title,
                    "description": task.description,
                    "done": task.done
                }
            } for task in tasks
        ]
    }

@router.get("/tasks/{task_id}", response_model=dict)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.is_deleted == False).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {
        "data": {
            "type": "task",
            "id": task.id,
            "attributes": {
                "title": task.title,
                "description": task.description,
                "done": task.done
            }
        }
    }

@router.put("/tasks/{task_id}", response_model=dict)
def update_task(task_id: int, task_data: schemas.TaskUpdateRequest, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.is_deleted == False).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    for key, value in task_data.data.attributes.dict().items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return {
        "data": {
            "type": "task",
            "id": task.id,
            "attributes": {
                "title": task.title,
                "description": task.description,
                "done": task.done
            }
        }
    }

@router.patch("/tasks/{task_id}", response_model=dict)
def patch_task(task_id: int, task_data: schemas.TaskUpdateRequest, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.is_deleted == False).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    for key, value in task_data.data.attributes.dict(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return {
        "data": {
            "type": "task",
            "id": task.id,
            "attributes": {
                "title": task.title,
                "description": task.description,
                "done": task.done
            }
        }
    }

@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.is_deleted == False).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    task.is_deleted = True
    db.commit()
    return

@router.get("/tasks/deleted/", response_model=dict)
def read_deleted_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).filter(models.Task.is_deleted == True).all()
    return {
        "data": [
            {
                "type": "task",
                "id": task.id,
                "attributes": {
                    "title": task.title,
                    "description": task.description,
                    "done": task.done
                }
            } for task in tasks
        ]
    }

@router.patch("/tasks/{task_id}/restore", response_model=dict)
def restore_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.is_deleted == True).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found or not deleted")
    task.is_deleted = False
    db.commit()
    db.refresh(task)
    return {
        "data": {
            "type": "task",
            "id": task.id,
            "attributes": {
                "title": task.title,
                "description": task.description,
                "done": task.done
            }
        }
    }
