"""Connecting the Front-End and the Back-End using FastAPI"""

from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    # mock before linking to backend
    name: str

db: dict[str, Task] = {"brush teeth": Task(name="brush teeth")}
# have habits already populated

# access paths

@app.post("/{task_name}")
def new_task(task: Task):
    # add to database
    # return success

@app.get("/{task_name}")
def access_task(task_name: str) -> Task:
    # return full task

@app.patch("/{task_name}")
def check_off(task_name: str) -> Task:
    # change done to true
    # return full task

@app.delete("/{task_name}")
def access_task(task_name: str) -> Task:
    # confirm if habit, do you want to delete this reoccuring habit?
    # delete task
    # return success

@app.get("/")
def access_task_list() -> list[str]:
    # run through database, extract name, add to list to be returned

# TODO: reordering