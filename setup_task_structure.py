import os

# Define base paths
base_dir = os.path.join(os.getcwd(), "models")
tasks_dir = os.path.join(base_dir, "tasks")

# Define file paths and default content
files = {
    os.path.join(tasks_dir, "__init__.py"): "",
    os.path.join(tasks_dir, "base_task.py"): '''from abc import ABC, abstractmethod
from datetime import datetime

class BaseTask(ABC):
    def __init__(self, title: str, due_date: datetime):
        self.title = title
        self.due_date = due_date
        self.created_at = datetime.now()
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def is_overdue(self):
        return not self.completed and datetime.now() > self.due_date

    @abstractmethod
    def get_reward(self) -> int:
        pass

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"[{{status}}] {{self.title}} (Due: {{self.due_date.strftime('%Y-%m-%d %H:%M')}})"
''',

    os.path.join(tasks_dir, "simple_task.py"): '''from models.tasks.base_task import BaseTask

class SimpleTask(BaseTask):
    def get_reward(self) -> int:
        return 10 if not self.is_overdue() else 1
''',

    os.path.join(base_dir, "task_manager.py"): '''from typing import List
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
'''
}

# Create directories if they don't exist
os.makedirs(tasks_dir, exist_ok=True)

# Create files with content
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Task module structure created successfully.")
