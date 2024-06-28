# 9.3.6. Задача page 321
# Лукас строит веб-приложение социальной сети для своей курсовой работы.
# В этом приложении он использует именованные кортежи в моделях дан-ных.
# Допустим, проект содержит следующий класс на базе именованных 
# кортежей:
# from collections import namedtuple
# User = namedtuple("User", "first_name last_name age")user = User("John", "Smith", "39")
# Что произойдет при попытке сериализовать объект user?
# ПОДСКАЗКА Объект tuple сериализуется в JSON и становится массивом JSON после сериализации.

from collections import namedtuple
import json

User = namedtuple("User", "first_name last_name age")
user = User("John", "Smith", 39)

# Сериализация объекта user в JSON
json_data = json.dumps(user)
print(json_data)

print()
# Сериализация объекта user в JSON, сохраняя структуру именованного кортежа
json_data1 = json.dumps(user._asdict())
print(json_data1)