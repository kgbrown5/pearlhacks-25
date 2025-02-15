"""Business logic"""

class Task:

    task_name: str
    recurring: bool
    done: bool

    def __init__(self, name: str, recurring: bool):
        self.task_name = name
        self.recurring = recurring
        self.done = False