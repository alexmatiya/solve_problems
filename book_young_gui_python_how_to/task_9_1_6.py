# 9.1.6. Задача
# В ходе работы над картографическим приложением Зоя определяет класс Direction
# так, как показано в предыдущих разделах. В листинге 9.2 функция move_to
# определяется за пределами класса Direction, но Зое кажется, что эту функцию
# лучше определить как метод экземпляра. Помогите ей выполнить это
# преобразование.
# ПОДСКАЗКА Разместите функцию move_to в теле класса Direction. Не за-будьте,
# что у метода экземпляра первый аргумент self обозначает текущий
# экземпляр.

from enum import Enum


class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

    def __str__(self):
        return self.name.lower()

    def move_to(self, distance: float):
        message = f"Go to the {self.name.lower()} for {distance} miles"
        print(message)


direction = Direction.NORTH
direction.move_to(3)
