"""Business logic for user"""
from __future__ import annotations
from typing import List
from logic.tasks import Task
from pydantic import BaseModel

class User(BaseModel):

    name: str
    username: str
    percent_completed: float = 0.0
    tasks: List[Task] = []

    def get_task(self, name:str) -> Task:
        for task in self.tasks:
            if task.task_name == name:
                return task
        return None

    def add_task(self, name: str, recurr: bool) -> None:
        """Adding a task to do list."""
        self.tasks.append(Task(task_name=name, recurring=recurr, done=False))


    def toggle_completion(self, name: str) -> None:
        """Mark task as complete and move to bottom of list."""
        task: Task

        for specific_task in self.tasks:
            if specific_task.task_name == name:
                task = specific_task

        task.done = not task.done

        if task.done: # if marked as complete
            self.tasks.pop(self.tasks.index(task))
            self.tasks.append(task)

        else:
            # if marked as incomplete
            self.tasks.pop(self.tasks.index(task))
            self.tasks.insert(0, task)

        self.update_percent_completed()

    def move_task_up(self, task: Task) -> None:
        """When up botton is clicked, moves task to index before current position."""
        old_pos: int = self.tasks.index(task)
        new_pos: int = old_pos - 1

        self.tasks[old_pos] = self.tasks[new_pos]
        self.tasks[new_pos] = task

    def move_task_down(self, task: Task) -> None:
        """When down botton is clicked, triggers task to move down one in list."""
        old_pos: int = self.tasks.index(task)
        new_pos: int = old_pos + 1

        self.tasks[old_pos] = self.tasks[new_pos]
        self.tasks[new_pos] = task


    def delete_task(self, task:Task) -> None:
        self.tasks.pop(self.tasks.index(task))

    
    def reset_list(self) -> None:
        """When day resets, remove daily tasks and keep recurring ones."""
        i: int = 0
        while (i < len(self.tasks)):
            if (self.tasks[i].recurring):
                i+=1
            else:
                self.tasks.pop(i) # if not recurring, remove when reset
        
    """Functions that the user doesn't call outright (side effects)"""
    def update_percent_completed(self) -> float:
        if (not self.tasks or len(self.tasks) == 0) : # catch errors with empty lists
            return 0.0 
        else:
            completed: int = 0
            for task in self.tasks:
                if task.recurring:
                    completed += 1

            return (float)(completed / len(self.tasks) * 100)
    