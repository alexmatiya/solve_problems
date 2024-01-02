# Реализуйте функцию spell(), которая принимает произвольное количество позиционных аргументов-слов и возвращает словарь, ключи которого — первые буквы слов, а значения — максимальные длины слов на эту букву.

# Примечание 1. Если в функцию не передается ни одного аргумента, функция должна возвращать пустой словарь.

# Примечание 2. Функция должна игнорировать регистр слов, при этом в результирующий словарь должны попасть именно буквы в нижнем регистре.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию, но не код, вызывающий ее.


def spell(*args):
    result = {}
    for word in args:
        first_letter = word[0].lower()
        if first_letter in result:
            result[first_letter] = max(result[first_letter], len(word))
        else:
            result[first_letter] = len(word)
    return result


assert (spell('Математика', 'История', 'химия', 'биология', 'Информатика')) == {'м': 10, 'и': 11, 'х': 5, 'б': 8}
assert (spell('fruit', 'football', 'February', 'forest', 'Family')) == {'f': 8}
