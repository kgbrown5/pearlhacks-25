"""Business logic"""

class Task:

    task_name: str
    recurring: bool
    done: bool

    def __init__(self, name: str, recurring: bool):
        self.task_name = name
        self.recurring = recurring
        self.done = False

tasks = []

def add_task(task: Task) -> None:
    """Adding a task to do list."""
    tasks.append(task)


def complete_task(task: Task) -> None:
    """Mark task as complete and move to bottom of list."""
    task.done = True
    tasks.pop(tasks.index(task))
    tasks.append(task)

def move_task_up(task: Task) -> None:
    """When up botton is clicked, moves task to index before current position."""
    old_pos: int = tasks.index(task)
    new_pos: int = old_pos - 1

    tasks[old_pos] = tasks[new_pos]
    tasks[new_pos] = task

def move_task_down(task: Task) -> None:
    """When down botton is clicked, triggers task to move down one in list."""
    old_pos: int = tasks.index(task)
    new_pos: int = old_pos + 1

    tasks[old_pos] = tasks[new_pos]
    tasks[new_pos] = task


def reset_list() -> None:
    """When day resets, remove daily tasks and keep recurring ones."""
    for t in tasks:
        if (not t.recurring):
            tasks.pop(tasks.index(t)) # if not recurring, remove when reset