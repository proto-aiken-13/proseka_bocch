from datetime import datetime, timedelta
from models.task_manager import TaskManager
from models.tasks.simple_task import SimpleTask

def test_add_task():
    manager = TaskManager()
    due = datetime.now() + timedelta(days=1)
    task = manager.add_task("Complete pytest test", due)

    assert isinstance(task, SimpleTask)
    assert task.title == "Complete pytest test"
    assert task.due_date == due
    assert not task.completed
    assert len(manager.tasks) == 1

def test_complete_task():
    manager = TaskManager()
    task = manager.add_task("Finish command parser", datetime.now() + timedelta(hours=3))

    assert not task.completed
    success = manager.complete_task(0)
    assert success
    assert task.completed

def test_list_tasks():
    manager = TaskManager()
    manager.add_task("T1", datetime.now())
    manager.add_task("T2", datetime.now())

    task_list = manager.list_tasks()
    assert len(task_list) == 2
    assert task_list[0].title == "T1"
    assert task_list[1].title == "T2"
