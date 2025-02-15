"""Connecting the Front-End and the Back-End using FastAPI"""

from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel
from logic.tasks import Task
from logic.user import User

app = FastAPI()

# class User(BaseModel): name: str
db: dict[str, User] = []

# examples to model functionality
caroline: User = User("Caroline", "cgbryan")
caroline.add_task("Stats homework", False)
caroline.add_task("Host office hours", True)

db[caroline.username] = caroline

katie: User = User("katie", "kgbrown5")
katie.add_task("Host office hours", True)
katie.add_task("Stats homework", False)

db[katie.username] = katie


@app.post("/{username}/{task_name}")
def new_task(username: str, task_name: str):
    return
    #TODO how to make recurring?
    # add to database
    # return success


@app.get("/{username}/{task_name}")
def access_task(username: str, task_name: str) -> Task:
    # finds task based on title
    return db[username].get_task(task_name)

@app.patch("/{username}/{task_name}")
def toggle_check(username: str, task_name: str) -> Task:
    task = db[username].get_task(task_name)
    task.toggle_completion()
    return task

@app.delete("/{username}/{task_name}")
def delete_task(username: str, task_name: str) -> Task:
    db[username].delete_task(db[username].get_task(task_name))
    # TODO return success

@app.get("/{username}")
def access_task_list(username: str) -> list[str]:
    return db[username].tasks
    # run through database, extract name, add to list to be returned
    # TODO probs not safe to return own list

# TODO: reordering