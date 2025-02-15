"""Business logic for user"""

class User:

    name: str
    username: str
    percent_completed: float
    tasks = []


    def __init__(self, name: str, username: str):
        self.name = name
        self.username = username
        self.percent_completed = 0.0


    
    

    
