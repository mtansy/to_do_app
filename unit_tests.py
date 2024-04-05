# test_todo_app.py

import unittest
from unittest.mock import patch
from io import StringIO
from toDoList import ToDoList

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = ToDoList()
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")

    def test_add_task(self):
        self.todo_list.add_task("Task 3")
        self.assertEqual(len(self.todo_list.get_tasks()), 3)

    def test_delete_task(self):
        self.todo_list.delete_task("Task 1")
        self.assertEqual(len(self.todo_list.get_tasks()), 1)

    def test_delete_nonexistent_task(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.todo_list.delete_task("Task 3")
            self.assertEqual(fake_out.getvalue().strip(), "Task not found!")

if __name__ == '__main__':
    unittest.main()
