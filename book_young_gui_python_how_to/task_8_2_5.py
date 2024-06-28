# 8.2.5. Задача page 276
# Продолжая работать над таск-менеджером, Леа осознает, что ей нужно создать
# экземпляр класса Task на основе объекта tuple: ("Laundry", "Wash clothes", 3)
# . Какую разновидность метода ей следует реализовать, чтобы обеспечить эту
# возможность в классе?
# ПОДСКАЗКА В листинге 8.6 приведена реализация метода, который создает
# экземпляр на основе объекта dict.


class Task:
    def __init__(self, title, description, tags=None):
        self.title = title
        self.description = description
        self.tags = [] if tags is None else tags

    @classmethod
    def from_tuple(cls, task_tuple):
        title, description, *tags = task_tuple
        return cls(title, description, tags)


task_tuple = ("Laundry", "Wash clothes", 3)
task = Task.from_tuple(task_tuple)
print(task.title)  # Output: Laundry
print(task.description)  # Output: Wash clothes
print(task.tags)  # Output: [3]