# test_todo_app.py
#test comment
import unittest
from unittest.mock import patch
from io import StringIO
from toDoList import ToDoList

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = ToDoList()
        self.todo_list.add_task("Task 1", 1)
        self.todo_list.add_task("Task 2", 3)

    def test_add_task(self):
        self.todo_list.add_task("Task 3", 2)
        self.assertEqual(len(self.todo_list.get_tasks()), 3)

    # https://stackoverflow.com/questions/33940432/how-to-sort-list-according-certain-criterion
    def test_get_by_priority(self):
        priority_list = [["Task 1", 1], ["Task 3", 2], ["Task 2", 3]]
        actual_list = [["Task 1", 1], ["Task 2", 3], ["Task 3", 2]]
        actual_list = sorted(actual_list,key= lambda x: x[1],reverse=False)

        self.assertEqual(actual_list, priority_list)


    def test_delete_task(self):
        self.todo_list.delete_task("Task 1")
        self.assertEqual(len(self.todo_list.get_tasks()), 1)

    def test_delete_nonexistent_task(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.todo_list.delete_task("Task 3")
            self.assertEqual(fake_out.getvalue().strip(), "Task not found!")

if __name__ == '__main__':
    unittest.main()