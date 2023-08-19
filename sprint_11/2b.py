# https://contest.yandex.ru/contest/23389/problems/B/
"""
B. Чётные и нечётные числа
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку, и
на экране появляются три случайных числа. Если все три числа оказываются одной
чётности, игрок выигрывает.

Напишите программу, которая по трём числам определяет, выиграл игрок или нет.

Формат ввода
В первой строке записаны три случайных целых числа a, b и c. Числа не
 превосходят 109 по модулю.

Формат вывода
Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.
"""


def check_parity(a: int, b: int, c: int) -> bool:
    if (a % 2 == 0 and b % 2 == 0 and c % 2 == 0) or (
            a % 2 == 1 and b % 2 == 1 and c % 2 == 1):
        return True


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


def main():
    a, b, c = map(int, input().strip().split())
    print_result(check_parity(a, b, c))


if __name__ == '__main__':
    main()
