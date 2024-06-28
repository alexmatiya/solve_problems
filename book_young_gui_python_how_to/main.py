class Task:
    def __new__(cls, *args):
        new_task = object.__new__(cls)
        print(f"__new__ is called, creating an instance at {id(new_task)}")
        return new_task

    def __init__(self, title):
        self.title = title
        print(f"__init__ is called, initializing an instance at {id(self)}")


task = Task("Laundry")

import sys
print(sys.getrefcount(task))
work = {"to_do": task}
print(sys.getrefcount(task))
tasks = [task]
print(sys.getrefcount(task))