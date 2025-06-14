from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    done = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False, nullable=False) 
