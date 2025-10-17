import json
import os
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task():
    title = input("Enter task title: ").strip()
    if title:
        task = {
            "title": title,
            "done": False,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Title cannot be empty.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    print("\n--- Task List ---")
    for idx, task in enumerate(tasks, 1):
        status = "✔️" if task["done"] else "❌"
        print(f"{idx}. [{status}] {task['title']} (Created: {task['created']})")

def mark_done():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to mark.")
        return
    view_tasks()
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    while True:
        print("\n=== Daily Task Tracker ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
