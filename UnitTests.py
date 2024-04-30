# File: test_todo_app.py
import unittest
from to_do import ToDoList
from unittest.mock import patch
from io import StringIO

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = ToDoList()
        self.todo_list.add_task("Task 1", 1)
        self.todo_list.add_task("Task 2", 3)

    def test_add_task(self):
        self.todo_list.add_task("Task 3", 2)
        self.assertEqual(len(self.todo_list.get_tasks()), 3)

    def test_delete_task(self):
        self.todo_list.delete_task("Task 1")
        self.assertEqual(len(self.todo_list.get_tasks()), 1)

    def test_delete_nonexistent_task(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.todo_list.delete_task("Task 3")
            self.assertEqual(fake_out.getvalue().strip(), "Task not found!")

    def test_get_tasks(self):
        tasks = self.todo_list.get_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0], ["Task 1", 1])
        self.assertEqual(tasks[1], ["Task 2", 3])

    def test_get_tasks_with_priority(self):
        # Example task list to sort by priority
        self.todo_list.add_task("Task 3", 2)

        # Get and sort tasks by priority (ascending order)
        tasks = sorted(self.todo_list.get_tasks(), key=lambda x: x[1])

        expected_tasks = [
            ["Task 1", 1],
            ["Task 3", 2],
            ["Task 2", 3]
        ]

        self.assertEqual(tasks, expected_tasks)

    def test_duplicate_task(self):
        # Adding the same task should create a duplicate
        self.todo_list.add_task("Task 1", 5)  # Same task with a different priority
        tasks = self.todo_list.get_tasks()

        # Check if the task is duplicated
        task_names = [task[0] for task in tasks]
        self.assertEqual(task_names.count("Task 1"), 2)

    def test_priority_change(self):
        # Update the priority by deleting and re-adding
        self.todo_list.delete_task("Task 1")
        self.todo_list.add_task("Task 1", 10)  # New priority

        tasks = self.todo_list.get_tasks()
        task_priorities = {task[0]: task[1] for task in tasks}

        self.assertEqual(task_priorities["Task 1"], 10)

if __name__ == '__main__':
    unittest.main()