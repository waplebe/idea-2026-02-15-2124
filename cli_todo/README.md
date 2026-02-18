# Simple CLI Todo List

This is a command-line tool for managing a todo list. It allows you to add tasks, view existing tasks, and persist them to a file.

## Features

*   **Add Tasks:**  Add multiple tasks at once.
*   **View Tasks:** Display the current list of tasks.
*   **Persistence:** Tasks are saved to a file (`todo.txt`) and loaded when the application starts.
*   **Error Handling:** Provides basic error messages for empty task lists.

## Usage

1.  **Add Tasks:**
    Run the script with the task(s) as arguments:

    ```bash
    python main.py task1 task2 task3
    ```

    This will print the list of tasks to the console and save them to `todo.txt`.

2.  **View Tasks:**
    Run the script without arguments:

    ```bash
    python main.py
    ```

    This will read the tasks from `todo.txt` and print them to the console.

## Installation

1.  Save the code as `main.py` in a directory named `cli_todo`.
2.  Open a terminal and navigate to the `cli_todo` directory.
3.  Run the script using `python main.py`.

## Example

```bash
python main.py "Buy groceries" "Walk the dog" "Finish report"
```

Output:

```
Tasks:
- Buy groceries
- Walk the dog
- Finish report
```

## Testing

The project includes unit tests to ensure the functionality of the `main.py` script.  To run the tests, navigate to the `cli_todo` directory in your terminal and execute:

```bash
python -m unittest discover -s tests
```

## Bug Fixes

*   **Issue 1:** The original script did not handle the case where no tasks were provided.  This has been fixed by adding a check for an empty task list and printing an appropriate message.
*   **Issue 2:** The original script did not handle multiple tasks being added at once. This has been fixed by accepting multiple arguments using `nargs='+'`.
*   **Issue 3:** The original script did not provide any persistence. This has been fixed by saving the tasks to a file (`todo.txt`).

## Improvements

*   **Error Handling:** Added basic error handling for empty task lists.
*   **Persistence:** Implemented file persistence to store tasks between sessions.
*   **Multiple Task Support:**  Allows adding multiple tasks at once.