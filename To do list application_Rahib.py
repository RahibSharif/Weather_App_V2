tasks = []

def add_task(task):
    tasks.append(task)
    print("Task successfully added")

def view_tasks():
    if not tasks:
        print("No task to view")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(task_number):
    try:
        tasks.pop(task_number - 1)
        print("Task successfully removed")
    except IndexError:
        print("Enter a vilid index")

while True:
    print("\\n To-do list menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove tasks")
    print("4. Exit")

    choice = input("Enter a choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        try:
            task_number = int(input("Enter a tasknumber to remove: "))
            remove_task(task_number)
        except ValueError:
            print("Invalid number")
    elif choice == "4":
        print("Exit the program")
        break
    else:
        print("Invalid choice")
