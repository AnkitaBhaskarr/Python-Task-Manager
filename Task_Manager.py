import os
import csv
import json

FILE_NAME = "tasks.txt"


def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(" | ")
                if len(data) == 5:
                    task_id, title, status, priority, deadline = data
                    tasks[int(task_id)] = {
                        "title": title,
                        "status": status,
                        "priority": priority,
                        "deadline": deadline
                    }
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(
                f"{task_id} | {task['title']} | "
                f"{task['status']} | "
                f"{task['priority']} | "
                f"{task['deadline']}\n"
            )


def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter Priority (High/Medium/Low): ").capitalize()
    deadline = input("Enter Deadline (DD-MM-YYYY): ")

    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {
        "title": title,
        "status": "Incomplete",
        "priority": priority,
        "deadline": deadline
    }
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== TASK LIST ==========")
    for task_id, task in tasks.items():
        print(
            f"[{task_id}] {task['title']} | "
            f"Status: {task['status']} | "
            f"Priority: {task['priority']} | "
            f"Deadline: {task['deadline']}"
        )


def mark_task_complete(tasks):
    try:
        task_id = int(input("Enter Task ID to mark as complete: "))
    except ValueError:
        print("Invalid Task ID.")
        return

    if task_id in tasks:
        tasks[task_id]["status"] = "Complete"
        print("Task marked as complete.")
    else:
        print("Task ID not found.")


def delete_task(tasks):
    try:
        task_id = int(input("Enter Task ID to delete: "))
    except ValueError:
        print("Invalid Task ID.")
        return

    if task_id in tasks:
        deleted = tasks.pop(task_id)
        print(f"Deleted: {deleted['title']}")
    else:
        print("Task ID not found.")


def export_csv(tasks):
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Task ID", "Title", "Status", "Priority", "Deadline"])
        for task_id, task in tasks.items():
            writer.writerow([
                task_id,
                task["title"],
                task["status"],
                task["priority"],
                task["deadline"]
            ])
    print("Exported to tasks.csv")


def export_json(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print("Exported to tasks.json")


def main():
    tasks = load_tasks()

    while True:
        print("\n========== TASK MANAGER ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Export to CSV")
        print("6. Export to JSON")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            export_csv(tasks)
        elif choice == "6":
            export_json(tasks)
        elif choice == "7":
            save_tasks(tasks)
            print("Thank you for using Task Manager!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()