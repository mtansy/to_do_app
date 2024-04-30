# File: todo_cli.py
import argparse
from to_do import ToDoList  # Import the ToDoList class from the appropriate module or file

def main():
    todo = ToDoList()

    # Define the command-line parser
    parser = argparse.ArgumentParser(description='Simple CLI for a ToDo List.')
    subparsers = parser.add_subparsers(title='Commands', dest='command')

    # Command to add a task
    add_parser = subparsers.add_parser('add', help='Add a new task.')
    add_parser.add_argument('task', type=str, help='Task description.')
    add_parser.add_argument('priority', type=int, help='Task priority.')

    # Command to delete a task
    delete_parser = subparsers.add_parser('delete', help='Delete a task.')
    delete_parser.add_argument('task', type=str, help='Task description to delete.')

    # Command to list all tasks
    list_parser = subparsers.add_parser('list', help='List all tasks.')

    # Parse the command-line arguments
    args = parser.parse_args()

    if args.command == 'add':
        # Add the specified task with the given priority
        todo.add_task(args.task, args.priority)
        print(f'Task "{args.task}" with priority {args.priority} added.')

    elif args.command == 'delete':
        # Delete the specified task
        todo.delete_task(args.task)
        print(f'Task "{args.task}" deleted.')

    elif args.command == 'list':
        # List all tasks
        tasks = todo.get_tasks()
        if tasks:
            print("Tasks:")
            for task, priority in tasks:
                print(f"- {task} (Priority: {priority})")
        else:
            print("No tasks in the list.")

if __name__ == '__main__':
    main()