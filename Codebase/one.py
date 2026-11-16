"""Daily Task Manager - PS No. 27
Console app: add tasks, view by priority, show pending, complete tasks.
Tasks are stored in tasks.txt (one task per line, fields separated by |).
"""

from datetime import datetime
import os

FILE_NAME = "tasks.txt"
PRIORITIES = ["High", "Medium", "Low"]
PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}

tasks = []  # list of dictionaries


# ---------- File handling ----------
def load_tasks():
    """Load tasks from the file at program start."""
    tasks.clear()
    if not os.path.exists(FILE_NAME):
        return
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 5:
                tasks.append({
                    "id": parts[0],
                    "title": parts[1],
                    "priority": parts[2],
                    "due": parts[3],
                    "status": parts[4],
                })


def save_tasks():
    """Save all tasks to the file (called after every change)."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(f"{t['id']}|{t['title']}|{t['priority']}|{t['due']}|{t['status']}\n")


# ---------- Helpers ----------
def next_id():
    """Task IDs start from T101 and always increase."""
    if not tasks:
        return "T101"
    highest = max(int(t["id"][1:]) for t in tasks)
    return f"T{highest + 1}"


def valid_date(text):
    """Check the date is exactly YYYY-MM-DD and a real date."""
    if len(text) != 10:
        return False
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def show_task(t):
    print(f"{t['id']} | {t['title']} | {t['priority']} | {t['due']} | {t['status']}")


def count_pending():
    return sum(1 for t in tasks if t["status"] == "Pending")


# ---------- Main features ----------
def add_task():
    title = input("Title: ").strip().replace("|", "/")
    if not title:
        print("Title cannot be empty.")
        return

    priority = input("Priority: ").strip().capitalize()
    if priority not in PRIORITIES:
        print("Invalid priority. Enter High, Medium or Low.")
        return

    due = input("Due: ").strip()
    if not valid_date(due):
        print("Invalid date. Use YYYY-MM-DD.")
        return

    task = {
        "id": next_id(),
        "title": title,
        "priority": priority,
        "due": due,
        "status": "Pending",
    }
    tasks.append(task)
    save_tasks()
    print("Task added.")
    show_task(task)


def view_by_priority():
    if not tasks:
        print("No tasks found.")
        return
    ordered = sorted(tasks, key=lambda t: (PRIORITY_ORDER[t["priority"]], t["due"]))
    for t in ordered:
        print(f"{t['id']} | {t['title']} | {t['priority']} | {t['due']}")


def show_pending():
    pending = [t for t in tasks if t["status"] == "Pending"]
    if not pending:
        print("No pending tasks. You are all caught up!")
        return
    for t in pending:
        show_task(t)


def complete_task():
    task_id = input("Enter task ID to complete: ").strip().upper()
    for t in tasks:
        if t["id"] == task_id:
            if t["status"] == "Done":
                print(f"Task {task_id} is already done.")
                return
            t["status"] = "Done"
            save_tasks()
            print(f"Task {task_id} marked as done. Pending tasks: {count_pending()}")
            return
    print(f"Task {task_id} not found.")


# ---------- Menu ----------
def main():
    load_tasks()
    while True:
        print("\n===== Daily Task Manager =====")
        print("1. Add task")
        print("2. View by priority")
        print("3. Show pending")
        print("4. Complete task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_by_priority()
        elif choice == "3":
            show_pending()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1-5.")


if __name__ == "__main__":
    main()