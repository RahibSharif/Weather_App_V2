import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
tasks_path = BASE_DIR / "tasks.json"

with open(tasks_path, "r") as f:
    tasks = json.load(f)

while True:
    option = input(f"""Choose option:  1. Add tasks., 2. View tasks. 3. Delete tasks. 4. Mark complete. 5. Quit. """)
    
    if option == "1":
        task = input("Enter a task: ")
        tasks.append({
            "task": task,
            "completed": False
        })

        with open(tasks_path, "w") as f:
            json.dump(tasks, f)

    elif option == "2":
        for i , task in enumerate(tasks, start = 1):
            status = "x" if task["completed"] == True else " "
            print(f"{i}. [{status}] {task['task']}")
    
    elif option == "3":
        task_num = int(input("Enter the task number to delete: "))
        del tasks[task_num - 1]

        with open(tasks_path, "w") as f:
            json.dump(tasks, f)

    elif option == "4":
        task_num = int(input("Enter the task number to mark complete: "))
        tasks[task_num -1]["completed"] = True

        with open(tasks_path, "w") as f:
            json.dump(tasks, f)

    elif option == "5":
        print("Goodbye!")
        break

    else:
        print("Sorry, there is an error")