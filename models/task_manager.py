from typing import List
from models.tasks.simple_task import SimpleTask
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks: List[SimpleTask] = []

    def add_task(self, title: str, due_date: datetime):
        task = SimpleTask(title, due_date)
        self.tasks.append(task)
        return task

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            return True
        return False

    def list_tasks(self):
        return self.tasks
