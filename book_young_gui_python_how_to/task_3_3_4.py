# 3.3.4. Задача page 102
# Допустим, в таск-менеджере требуется обновить именованный кортеж Task(title='Laundry', desc='Wash clothes',
# urgency=3), установив для него степень срочности (urgency) равной 4. Можно ли изменить степень напрямую?
# Если нет, то как это можно сделать?
# ПОДСКАЗКА Именованный кортеж представляет собой объект кортежа, поэтому он неизменяем и прямое изменение
# хранимых в нем данных недо-
# пустимо.

# 1. Использование метода _replace():

from collections import namedtuple

Task = namedtuple("Task", ["title", "desc", "urgency"])
task = Task(title="Laundry", desc="Wash clothes", urgency=3)
updated_task = task._replace(urgency=4)

print(task)  # Task(title='Laundry', desc='Wash clothes', urgency=3)
print(updated_task)  # Task(title='Laundry', desc='Wash clothes', urgency=4)

# 2. Использование распаковки и создание нового кортежа:

task = Task(title="Laundry", desc="Wash clothes", urgency=3)
updated_task = Task(title=task.title, desc=task.desc, urgency=4)

print(task)  # Task(title='Laundry', desc='Wash clothes', urgency=3)
print(updated_task)  # Task(title='Laundry', desc='Wash clothes', urgency=4)
