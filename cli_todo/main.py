import argparse

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
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        
        with open("todo.txt", "w") as f:
            for task in tasks:
                if task.startswith(task_to_complete):
                    f.write(f"{task.strip()} (complete)\n")
                else:
                    f.write(task.strip() + "\n")
        return

    if args.priority:
        task_to_prioritize = args.priority
        print(f"Setting priority for task to {task_to_prioritize}")
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        
        with open("todo.txt", "w") as f:
            for task in tasks:
                if task.startswith(task_to_prioritize):
                    f.write(f"{task.strip()} ({task_to_prioritize})\n")
                else:
                    f.write(task.strip() + "\n")
        return

    print("Tasks:")
    for task in args.task:
        print(f"- {task} ({args.priority if args.priority else 'Low'})")

    # Add persistence using a simple file
    with open("todo.txt", "a") as f:
        for task in args.task:
            f.write(f"{task}\n")

if __name__ == "__main__":
    main()