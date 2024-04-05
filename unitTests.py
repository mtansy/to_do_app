# unit_tests.py
import unittest
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

    def test_get_tasks(self):
        tasks = self.todo_list.get_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn("Task 1", tasks)
        self.assertIn("Task 2", tasks)

if __name__ == '__main__':
    unittest.main()
