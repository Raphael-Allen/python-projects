import json

class ToDoList:

    def __init__(self):
        self.welcome = "Welcome to you To Do List!"
        self.tasks = []
        self.load_tasks()

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []
    def run(self):
        while True:
            self.selector = input("1. Add task 2. Remove task 3. View tasks 4. Quit ")
            if self.selector == "1":
                self.add_task()
            elif self.selector == "2":
                self.remove_task()
            elif self.selector == "3":
                self.view_tasks()
            elif self.selector == "4":
                return
            else:
                print("Error: Input invalid")

    def add_task(self):
        while True:
            new_task = input("Add your new task")
            self.tasks.append(new_task)
            again = input("Press 1.Add another task 2.Main menu ")
            if again == "1":
                pass
            elif again == "2":
                self.save_tasks()
                return
            else:
                print("Error: Input invalid")
                continue

    def remove_task(self):
        if len(self.tasks) < 1:
            print("No tasks to remove")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(index, task)
        try:
            remove = int(input("Select task to remove by entering it's corresponding number "))
            if remove < 1:
                print("Error: please enter a positive number")
            else:
                self.tasks.pop(remove -1)
                print("Task removed!")
        except ValueError:
            print("Error: Please enter a number")
        except IndexError:
            print("Error: Task number does not exist")
        for index, task in enumerate(self.tasks, start=1):
            print(index, task)
        self.save_tasks()

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks to view")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(index, task)

ToDo = ToDoList()           # force a save
ToDo.run()