# Simple CLI Todo List

This is a very basic command-line tool for managing a todo list.

## Usage

To add tasks, run the script with the task(s) as arguments:

```bash
python main.py task1 task2 task3
```

This will print the list of tasks to the console.  The tasks are also saved to a file named `todo.txt` in the project directory.

To view the tasks, run the script without arguments:

```bash
python main.py
```

This will read the tasks from `todo.txt` and print them to the console.