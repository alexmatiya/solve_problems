# Реализуйте функцию convert(), которая принимает один аргумент:

# string — произвольная строка
# Функция должна возвращать строку string:

# полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
# полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
# полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает


def convert(text: str) -> str:
    lower = [i for i in text if i.islower()]
    upper = [i for i in text if i.isupper()]
    if len(lower) >= len(upper):
        return text.lower()
    else:
        return text.upper()


assert (convert("BEEgeek")) == "beegeek"
assert (convert("pyTHON")) == "PYTHON"
assert (convert("pi31415!")) == "pi31415!"
