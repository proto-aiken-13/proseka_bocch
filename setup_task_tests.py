import os

# Define base test directory
tests_dir = os.path.join(os.getcwd(), "tests")

# Define paths and test content
files = {
    os.path.join(tests_dir, "__init__.py"): "",
    os.path.join(tests_dir, "test_task_flow.py"): '''import sys
import os
from datetime import datetime, timedelta

# Add models directory to path for local imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.task_manager import TaskManager

def test_task_flow():
    manager = TaskManager()

    print("\\n🎯 Adding tasks...")
    t1 = manager.add_task("Finish bot skeleton", datetime.now() + timedelta(days=1))
    t2 = manager.add_task("Write !addtask command", datetime.now() + timedelta(hours=2))

    print("\\n📋 Current Tasks:")
    for idx, t in enumerate(manager.list_tasks()):
        print(f"{idx}.", t)

    print("\\n✅ Completing second task...")
    manager.complete_task(1)

    print("\\n📋 Updated Tasks:")
    for idx, t in enumerate(manager.list_tasks()):
        print(f"{idx}.", t)

if __name__ == "__main__":
    test_task_flow()
'''
}

# Create test directory
os.makedirs(tests_dir, exist_ok=True)

# Write test files
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Test structure for Task classes created successfully.")
