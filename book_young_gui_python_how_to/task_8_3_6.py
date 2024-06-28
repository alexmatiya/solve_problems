# 8.3.6. Задача page 285
# Допустим, атрибут urgency должен содержать целое значение от 1 до 5. Сможете
# ли вы преобразовать его в свойство при помощи сеттера? Сеттер позволяет
# про-верить присваиваемое значение.
# ПОДСКАЗКА Вы можете использовать защищенный атрибут (например, _urgency)
# для внутреннего представления данных urgency и создать свойство с именем urgency.


class Task:
    def __init__(self, title, desc, urgency):
        self.title = title
        self.desc = desc
        self._urgency = 1
        self._status = "created"

    @property
    def urgency(self):
        return self._urgency

    @urgency.setter
    def urgency(self, value):
        allowed_values = [1, 2, 3, 4, 5]
        if value in allowed_values:
            self._urgency = value
            print(f"task urgency set to: {value}")
        else:
            print(f"invalid urgency: {value}")


task = Task(title="Learn Python", desc="Learn Python", urgency=1)

task.urgency = 2
task.urgency = 6
