import argparse
import os
import json

def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list.")
    parser.add_argument("task", nargs='+', help="The task to add.")
    parser.add_argument("--complete", nargs='?', const="complete", help="Mark a task as complete.")
    parser.add_argument("--priority", nargs='?', const="High", help="Set the priority of a task (High, Medium, Low).")

    args = parser.parse_args()

    if not args.task:
        print("No tasks provided.")
        return

    if args.complete:
        task_to_complete = args.complete
        print(f"Marking task '{task_to_complete}' as complete.")
        try:
            with open("todo.json", "r") as f:
                tasks = json.load(f)
        except FileNotFoundError:
            tasks = []

        task_dict = {task: task for task in tasks}
        if task_to_complete in task_dict:
            del task_dict[task_to_complete]
            task_dict[task_to_complete] = f"{task_to_complete} (complete)"
        with open("todo.json", "w") as f:
            json.dump(list(task_dict.values()), f, indent=4)
        return

    if args.priority:
        task_to_prioritize = args.priority
        print(f"Setting priority for task to {task_to_prioritize}")
        try:
            with open("todo.json", "r") as f:
                tasks = json.load(f)
        except FileNotFoundError:
            tasks = []

        task_dict = {task: task for task in tasks}
        for task in task_dict:
            if task == task_to_prioritize:
                task_dict[task] = f"{task} ({task_to_prioritize})"
        with open("todo.json", "w") as f:
            json.dump(list(task_dict.values()), f, indent=4)
        return

    print("Tasks:")
    for task in args.task:
        print(f"- {task} ({args.priority if args.priority else 'Low'})")

    # Add persistence using a simple file
    try:
        with open("todo.json", "a") as f:
            for task in args.task:
                json.dump([task], f, indent=4)
                f.write('\n')
    except FileNotFoundError:
        with open("todo.json", "w") as f:
            json.dump(args.task, f, indent=4)


if __name__ == "__main__":
    main()