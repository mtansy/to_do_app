class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority):
        self.tasks.append([task, priority])

    def delete_task(self, task):
        for list in self.tasks:
            if task in list:
                self.tasks.remove(list)
                return
        print("Task not found!")

    def get_tasks(self):
        return self.tasks