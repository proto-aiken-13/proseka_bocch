from abc import ABC, abstractmethod
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
