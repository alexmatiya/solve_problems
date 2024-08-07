# 5.1.5. Задача page 161
# Ава, перспективный финансовый аналитик, изучает Python. Ей очень нравится функция zip, соединяющая несколько итераторов,
# и ей хотелось бы узнать, как zip работает с несколькими итерируемыми объектами. Помогите ей написать код для
# тестирования zip с тремя итерируемыми объектами.
# Количество элементов в разных итерируемых объектах тоже различается. Определите, что происходит при попытке соединения
# итерируемых объектов с разным количеством элементов функцией zip.
# ПОДСКАЗКА Два итерируемых объекта образуют двухэлементные кортежи после соединения. Если один итерируемый объект короче
# другого, то более короткий итерируемый объект не сможет предоставить компонент, когда его элементы будут полностью
# израсходованы.

from itertools import zip_longest

names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris", "Tokyo", "Sydney"]

# здесь выведет только 5 тупла, так как максимальный в зипе имеет 5 элементов: cities = ["New York", "London", "Paris", "Tokyo", "Sydney"] (пустые будут None)
result = list(zip_longest(names, ages, cities, fillvalue=None))
print(result)

# здесь выведет только 3 тупла, так как минимальный в зипе имеет 3 элемента: ages = [25, 30, 35]
result2 = list(zip(names, ages, cities))
print(result2)
