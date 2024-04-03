import sys
from toDoList import ToDoList

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add task")
        print("2. Delete task")
        print("3. View tasks")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            task = input("Enter task to delete: ")
            todo_list.delete_task(task)
        elif choice == '3':
            print("Tasks:")
            for task in todo_list.get_tasks():
                print(task)
        elif choice == '4':
            sys.exit("Exiting...")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()