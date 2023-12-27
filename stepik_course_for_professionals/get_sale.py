# Задача. Санта очень любит играть с числами. Он задумал посчитать сумму всех цифр в числах от 1 до 10**n (10 в степени n).
# При n = 2 он легко посчитал нужную сумму: 1 + 2 + 3 + … + (9 + 9) + (1 + 0 + 0) = 901.

# Скидка 45% 🚩🚩🚩: решите задачу Санты для n = 8, то есть посчитайте сумму цифр во всех числах от 1 до 100 000 000.

# Скидка 50% 🚩🚩🚩: решите задачу Санты для n = 18, то есть посчитайте сумму цифр во всех числах от 1 до 1 000 000 000 000 000 000.


def get_sale_fast(number: int) -> int:
    """Вычисляет сумму цифр в последовательности от 1 до 10 в степени number"""
    k = int(str(number) + str((number - 1) * "0"))
    result = sum(i * k for i in range(1, 10)) + 1
    print(f"Сумма цифр от 1 до 10 в степени {number} = {result}")


def get_sale(n: int) -> int:
    result = sum([int(j) for i in range(1, 10**n) for j in str(i)]) + 1
    print(f"Сумма цифр от 1 до 10 в степени {n} = {result}")


print("Быстрый способ:")
get_sale_fast(2)
get_sale_fast(8)
get_sale_fast(18)
print("-" * 50)
print("Медленный способ:")
get_sale(2)
# get_sale(8)
