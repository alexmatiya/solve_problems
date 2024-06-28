# 8.4.5. Задача page 290
# В классе Task метод __repr__ возвращает результат f"Task({self.title!r},{self.desc!r}, {self.urgency})".
# В этой f-строке жестко зафиксировано имя класса Task. Общий принцип программирования требует свести
# к минимуму фиксацию данных в коде. Как получить имя класса на программном уровне?
# ПОДСКАЗКА Экземпляр содержит специальный атрибут __class__, опре-деляющий его класс,
# а у класса имеется специальный атрибут __name__ для получения имени класса.

class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self._status = "created"

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed_values = ["created", "started", "completed", "suspended"]
        if value in allowed_values:
            self._status = value
            print(f"task status set to: {value}")
        else:
            print(f"invalid status: {value}")

    def __str__(self):
        return f"{self.title}: {self.desc}, urgency level {self.urgency}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title!r}, {self.desc!r}, {self.urgency})"


task = Task(title="Learn Python", desc="Learn Python", urgency=1)

task.status = "completed"
task.status = "completed1"
print(task)
print(repr(task))
print(eval(repr(task)))
