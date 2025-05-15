from models.tasks.base_task import BaseTask

class SimpleTask(BaseTask):
    def get_reward(self) -> int:
        return 10 if not self.is_overdue() else 1
