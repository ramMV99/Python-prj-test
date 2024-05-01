# task_manager.py

import sys

def main():
    print("Welcome to Task Manager!")
    print("Available commands:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Exit")

    tasks = []

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            task_name = input("Enter task name: ")
            tasks.append(task_name)
            print("Task added successfully!")
        elif choice == '2':
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        elif choice == '3':
            print("Exiting Task Manager...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
