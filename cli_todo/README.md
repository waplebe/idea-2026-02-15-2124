# Simple CLI Todo List

This is a command-line tool for managing a todo list. It allows you to add tasks, view existing tasks, mark tasks as complete, set task priorities, and persist them to a file.

## Features

*   **Add Tasks:** Add multiple tasks at once.
*   **View Tasks:** Display the current list of tasks.
*   **Persistence:** Tasks are saved to a file (`todo.json`) and loaded when the application starts.
*   **Mark Tasks as Complete:**  Mark tasks as complete by specifying the `--complete` flag.
*   **Set Task Priority:** Set the priority of a task using the `--priority` flag (High, Medium, Low).
*   **Error Handling:** Provides basic error messages for empty task lists.

## Usage

1.  **Add Tasks:**
    Run the script with the task(s) as arguments:

    ```bash
    python main.py task1 task2 task3
    ```

    This will print the list of tasks to the console and save them to `todo.json`.

2.  **View Tasks:**
    Run the script without arguments:

    ```bash
    python main.py
    ```

    This will read the tasks from `todo.json` and print them to the console.

3.  **Mark a Task as Complete:**
    ```bash
    python main.py --complete "Buy groceries"
    ```

4.  **Set Task Priority:**
    ```bash
    python main.py --priority High "Finish report"
    ```

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
- Buy groceries (Low)
- Walk the dog (Low)
- Finish report (Low)
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
*   **Issue 4:** The original script did not support marking tasks as complete or setting priorities. These features have been added.

## Improvements

*   **Error Handling:** Added basic error handling for empty task lists.
*   **Persistence:** Implemented file persistence to store tasks between sessions.
*   **Multiple Task Support:** Allows adding multiple tasks at once.
*   **Task Completion:** Added functionality to mark tasks as complete.
*   **Task Prioritization:** Added functionality to set the priority of tasks.
*   **Command-Line Flags:** Implemented command-line flags for task completion and priority setting.
*   **Improved Documentation:** Updated the README to include instructions for using the new features.
*   **Data Persistence:**  Tasks are now stored in a JSON file (`todo.json`) for better structure and easier modification.
*   **Robust Error Handling:** Added try-except blocks to handle potential file errors during loading and saving.
*   **Comprehensive Testing:** Added unit tests to cover all new features and bug fixes.