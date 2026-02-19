import unittest
import subprocess
import os

class TestMain(unittest.TestCase):

    def setUp(self):
        self.test_dir = "temp_test_dir"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_dir)

    def test_add_tasks(self):
        # Create a temporary todo.txt file
        todo_file = os.path.join(self.test_dir, "todo.txt")
        with open(todo_file, "w") as f:
            f.write("")

        # Run the script with tasks
        result = subprocess.run(["python", "main.py", "task1", "task2", "task3"], capture_output=True, text=True)

        # Assert that the output is correct
        self.assertEqual(result.stdout, "Tasks:\n- task1 (Low)\n- task2 (Low)\n- task3 (Low)\n")

        # Assert that the todo.txt file contains the tasks
        with open(todo_file, "r") as f:
            content = f.read()
        self.assertEqual(content, "task1\ntask2\ntask3\n")

    def test_view_tasks(self):
        # Create a temporary todo.txt file with some tasks
        todo_file = os.path.join(self.test_dir, "todo.txt")
        with open(todo_file, "w") as f:
            f.write("task1\ntask2\n")

        # Run the script without arguments
        result = subprocess.run(["python", "main.py"], capture_output=True, text=True)

        # Assert that the output is correct
        self.assertEqual(result.stdout, "Tasks:\n- task1 (Low)\n- task2 (Low)\n")

        # Assert that the todo.txt file contains the tasks
        with open(todo_file, "r") as f:
            content = f.read()
        self.assertEqual(content, "task1\ntask2\n")

    def test_no_tasks_provided(self):
        # Run the script without arguments
        result = subprocess.run(["python", "main.py"], capture_output=True, text=True)

        # Assert that the output is correct
        self.assertEqual(result.stdout, "No tasks provided.\n")

    def test_complete_task(self):
        # Create a temporary todo.txt file
        todo_file = os.path.join(self.test_dir, "todo.txt")
        with open(todo_file, "w") as f:
            f.write("task1\ntask2\n")

        # Run the script to complete a task
        result = subprocess.run(["python", "main.py", "--complete", "task1"], capture_output=True, text=True)

        # Assert that the output is correct
        self.assertEqual(result.stdout, "Marking task 'task1' as complete.\n")

        # Assert that the todo.txt file contains the updated task
        with open(todo_file, "r") as f:
            content = f.read()
        self.assertEqual(content, "task2\n")

    def test_priority_task(self):
        # Create a temporary todo.txt file
        todo_file = os.path.join(self.test_dir, "todo.txt")
        with open(todo_file, "w") as f:
            f.write("task1\ntask2\n")

        # Run the script to set priority
        result = subprocess.run(["python", "main.py", "--priority", "High", "task1"], capture_output=True, text=True)

        # Assert that the output is correct
        self.assertEqual(result.stdout, "Setting priority for task to task1.\n")

        # Assert that the todo.txt file contains the updated task
        with open(todo_file, "r") as f:
            content = f.read()
        self.assertEqual(content, "task1 (High)\ntask2\n")

if __name__ == '__main__':
    unittest.main()