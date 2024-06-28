# 3.4.7. Задача page 108
# Встроенная функция id проверяет адрес памяти, занимаемой объектом. Вызов id("Hello") вернет адрес объекта "Hello".
# Можно ли использовать функцию id для отслеживания изменений в таком объекте представления словаря, как dict_keys?
# Ожидается, что данные объекта представления будут изменяться 
# 3.5. Когда использовать словари и множества вместо списков и кортежей 109
# с обновлением объекта dict. С другой стороны, адрес памяти объекта пред-ставления должен оставаться неизменным.
# ПОДСКАЗКА Адрес памяти объекта остается постоянным на протяжении его жизненного цикла. Хотя данные объекта могут
# изменяться, адрес памяти меняться не должен.


# Answer:

# использование id() для отслеживания изменений в объектах представления словаря не будет работать, так как адрес
# памяти останется неизменным. Вместо этого, вам нужно будет отслеживать изменения непосредственно в словаре.

my_dict = {'a': 1, 'b': 2}
keys = my_dict.keys()
print(id(keys))  # Выведет какой-то адрес в памяти
my_dict['c'] = 3
print(id(keys))  # Адрес в памяти остался тем же
