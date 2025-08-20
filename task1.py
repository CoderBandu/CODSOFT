tasks = []

def show():
    if not tasks:
        print("\nNo tasks available!\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "DONE" if task["done"] else "UNDONE"
            print(f"{i}. {task['task']} [{status}]")
    print()

def add():
    task_name = input("Enter the task: ")
    tasks.append({"task": task_name, "done": False})
    print("Task added successfully!\n")

def mark_complete():
    show()
    task_no = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks[task_no]["done"] = True
        print("Task marked as complete!\n")
    else:
        print("Invalid task number!\n")

def delete():
    show()
    task_no = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks.pop(task_no)
        print("Task deleted successfully!\n")
    else:
        print("Invalid task number!\n")

while True:
    print("--------------------------------------")
    print("TO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show()
    elif choice == "2":
        add()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        delete()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")
