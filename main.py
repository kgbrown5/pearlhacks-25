"""Connecting the Front-End and the Back-End using FastAPI"""

from fastapi import FastAPI, status
# from logic.tasks import Task
from logic.user import User

app = FastAPI()

db: dict[str, User] = {}

# Example users
caroline = User(name="Caroline", username="cgbryan1")
caroline.add_task("Stats homework", False)
caroline.add_task("Host office hours", True)
db[caroline.username] = caroline

katie = User(name="Katie", username="kgbrown5")
katie.add_task("Host office hours", True)
katie.add_task("Stats homework", False)
db[katie.username] = katie

@app.post("/{username}/{task_name}")
def new_task(username: str, task_name: str, reoccur: bool):
    user = db.get(username)
    if not user:
        return {"error": "User not found."}, status.HTTP_404_NOT_FOUND
    
    user.add_task(task_name, reoccur)
    return {"message": "Task created successfully."}, status.HTTP_201_CREATED

@app.get("/{username}/{task_name}")
def access_task(username: str, task_name: str):
    user = db.get(username)
    if not user:
        return {"error": "User not found."}, status.HTTP_404_NOT_FOUND
    
    task = user.get_task(task_name)
    if not task:
        return {"error": "Task not found"}, status.HTTP_404_NOT_FOUND
    
    return task

@app.patch("/{username}/{task_name}")
def toggle_check(username: str, task_name: str):
    user = db.get(username)
    if not user:
        return {"error": "User not found."}, status.HTTP_404_NOT_FOUND
    
    task = user.get_task(task_name)
    if not task:
        return {"error": "Task not found"}, status.HTTP_404_NOT_FOUND
    
    task.toggle_completion()  # Task-level method
    return {"message": "Task completion toggled."}, status.HTTP_200_OK

@app.delete("/{username}/{task_name}")
def delete_task(username: str, task_name: str):
    user = db.get(username)
    if not user:
        return {"error": "User not found."}, status.HTTP_404_NOT_FOUND
    
    task = user.get_task(task_name)
    if not task:
        return {"error": "Task not found"}, status.HTTP_404_NOT_FOUND
    
    user.delete_task(task)
    return {"message": "Task deleted successfully."}, status.HTTP_204_NO_CONTENT

# Moving a task up or down
@app.patch("/{username}/{task_name}/{direction}")
def shift_position(username: str, task_name: str, direction: str):
    user = db.get(username)
    if not user:
        return {"error": "User not found."}, status.HTTP_404_NOT_FOUND
    
    task = user.get_task(task_name)
    if not task:
        return {"error": "Task not found"}, status.HTTP_404_NOT_FOUND
    
    direction = direction.lower()
    if direction == "up":
        user.move_task_up(task)
    elif direction == "down":
        user.move_task_down(task)
    else:
        return {"error": "Invalid direction"}, status.HTTP_400_BAD_REQUEST
    
    return {"message": "Task moved successfully."}, status.HTTP_200_OK

@app.get("/{username}")
def access_task_list(username: str):
    user = db.get(username)
    if not user:
        return {"error": "User not found."}, status.HTTP_404_NOT_FOUND
    
    return {"tasks": user.tasks}

@app.delete("/{username}")
def reset_list(username: str) -> None:
    user = db.get(username)
    if not user:
        return {"error": "User not found."}, status.HTTP_404_NOT_FOUND
    
    user.reset_list()
    return {"message": "Tasks cleared successfully."}, status.HTTP_200_OK