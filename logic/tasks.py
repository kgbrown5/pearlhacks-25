"""Business logic"""
from pydantic import BaseModel

class Task(BaseModel):
    task_name: str
    recurring: bool
    done: bool