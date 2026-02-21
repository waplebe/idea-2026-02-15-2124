import unittest
import subprocess
import os
import json

class TestMain(unittest.TestCase):

    def setUp(self):
        self.test_dir = "temp_test_dir"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_dir)

    def test_add_tasks(self):
        # Create a temporary todo.json file
        todo_file = os.path.join(self.test_dir, "todo.json")
        with open(todo_file, "w") as f:
            json.dump([], f, indent=4)

        # Run the script with tasks
        result = subprocess.run(["python", "main.py", "task1", "task2", "task3"], capture_output=True, text=True)

        # Assert that the output is correct
        self.assertEqual(result.stdout, "Tasks:\n- task1 (Low)\n- task2 (Low)\n- task3 (Low)\n")

        # Assert that the todo.json file contains the tasks
        with open(todo_file, "r") as f:
            content = json.load(f)
        self.assertEqual(content, ["task1", "task2", "task3"])

    def test_view_tasks(self):
        # Create a temporary todo.json file with some tasks
        todo_file = os.path.join(self.test_dir, "todo.json")
        with open(todo_file, "w") as f:
            json.dump(["task1", "task2"], f, indent=4)

        # Run the script without arguments
        result = subprocess.run(["python", "main.py"], capture_output=True, text=True)

        # Assert that the output is correct
        self.assertEqual(result.stdout, "Tasks:\n- task1 (Low)\n- task2 (Low)\n")

        # Assert that the todo.json file contains the tasks
        with open(todo_file, "r") as f:
            content = json.load(f)
        self.assertEqual(content, ["task1", "task2"])

    def test_no_tasks_provided(self):
        # Run the script without arguments
        result = subprocess.run(["python", "main.py"], capture_output=True, text=True)

        # Assert that the output is correct
        self.assertEqual(result.stdout, "No tasks provided.\n")

    def test_complete_task(self):
        # Create a temporary todo.json file
        todo_file = os.path.join(self.test_dir, "todo.json")
        with open(todo_file, "w") as f:
            json.dump(["task1", "task2"], f, indent=4)

        # Run the script to complete a task
        result = subprocess.run(["python", "main.py", "--complete", "task1"], capture_output=True, text=True)

        # Assert that the output is correct
        self.assertEqual(result.stdout, "Marking task 'task1' as complete.\n")

        # Assert that the todo.json file contains the updated task
        with open(todo_file, "r") as f:
            content = json.load(f)
        self.assertEqual(content, ["task2"])

    def test_priority_task(self):
        # Create a temporary todo.json file
        todo_file = os.path.join(self.test_dir, "todo.json")
        with open(todo_file, "w") as f:
            json.dump(["task1", "task2"], f, indent=4)

        # Run the script to set priority
        result = subprocess.run(["python", "main.py", "--priority", "High", "task1"], capture_output=True, text=True)

        # Assert that the output is correct
        self.assertEqual(result.stdout, "Setting priority for task to task1.\n")

        # Assert that the todo.json file contains the updated task
        with open(todo_file, "r") as f:
            content = json.load(f)
        self.assertEqual(content, ["task1 (High)", "task2"])

    def test_add_task_with_complete_flag(self):
        # Create a temporary todo.json file
        todo_file = os.path.join(self.test_dir, "todo.json")
        with open(todo_file, "w") as f:
            json.dump([], f, indent=4)

        # Run the script with a task and the --complete flag
        result = subprocess.run(["python", "main.py", "task1", "--complete", "task1"], capture_output=True, text=True)

        # Assert that the output is correct
        self.assertEqual(result.stdout, "Marking task 'task1' as complete.\n")

        # Assert that the todo.json file contains the updated task
        with open(todo_file, "r") as f:
            content = json.load(f)
        self.assertEqual(content, ["task1 (complete)"])

    def test_add_task_with_priority_flag(self):
        # Create a temporary todo.json file
        todo_file = os.path.join(self.test_dir, "todo.json")
        with open(todo_file, "w") as f:
            json.dump([], f, indent=4)

        # Run the script with a task and the --priority flag
        result = subprocess.run(["python", "main.py", "task1", "--priority", "High"], capture_output=True, text=True)

        # Assert that the output is correct
        self.assertEqual(result.stdout, "Setting priority for task to task1.\n")

        # Assert that the todo.json file contains the updated task
        with open(todo_file, "r") as f:
            content = json.load(f)
        self.assertEqual(content, ["task1 (High)"])