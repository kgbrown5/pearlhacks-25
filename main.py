"""Connecting the Front-End and the Back-End using FastAPI"""

from fastapi import FastAPI, status
from typing import Annotated
from pydantic import BaseModel
from logic.tasks import Task
from logic.user import User

app = FastAPI()

# class User(BaseModel): name: str
<<<<<<< HEAD
db: dict[str, User] = {}
=======
db: dict[str, User] = []
>>>>>>> ac283dd51cf29b5bd12579c49c12a19125566f6c

# examples to model functionality
caroline: User = User(name="Caroline", username="cgbryan1")
caroline.add_task("Stats homework", False)
caroline.add_task("Host office hours", True)

db[caroline.username] = caroline

katie: User = User(name="Katie", username="kgbrown5")
katie.add_task("Host office hours", True)
katie.add_task("Stats homework", False)

db[katie.username] = katie


@app.post("/{username}/{task_name}")
def new_task(username: str, task_name: str, reoccur: bool):
    db[username].add_task(task_name, reoccur)
    return status.HTTP_201_CREATED


@app.get("/{username}/{task_name}")
def access_task(username: str, task_name: str):
    return db[username].get_task(task_name)

@app.patch("/{username}/{task_name}")
def toggle_check(username: str, task_name: str):
    db[username].toggle_completion(task_name)
    return status.HTTP_200_OK

@app.delete("/{username}/{task_name}")
def delete_task(username: str, task_name: str):
    db[username].delete_task(db[username].get_task(task_name))
    return status.HTTP_204_NO_CONTENT

@app.get("/{username}")
def access_task_list(username: str) -> list[Task]:
    return db[username].tasks
    # TODO probs not safe to return own list

# TODO: reordering