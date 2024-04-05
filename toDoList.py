"""
This module defines a simple ToDoList class..
"""

class ToDoList:
    """
    A simple class to manage a ToDo list.
    """

    def __init__(self):
        """
        Initialize a new ToDoList instance.
        """
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the ToDo list.

        Args:
            task (str): The task to add.
        """
        self.tasks.append(task)

    def delete_task(self, task):
        """
        Delete a task from the ToDo list.

        Args:
            task (str): The task to delete.
        """
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found!")

    def get_tasks(self):
        """
        Get the list of tasks in the ToDo list.

        Returns:
            list: The list of tasks.
        """
        return self.tasks
