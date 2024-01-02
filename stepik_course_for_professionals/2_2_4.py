# Более одного
# Дана последовательность неотрицательных целых чисел. Напишите программу, которая выводит те числа, которые встречаются в данной последовательности более одного раза.

# Формат входных данных
# На вход программе подается строка, содержащая целые неотрицательные числа, разделенные пробелом.

# Формат выходных данных
# Программа должна вывести те числа, которые встречаются в данной строке более одного раза, разделяя их пробелом. Числа должны быть расположены в порядке возрастания и не должны повторяться.

# Примечание 1. Если повторяющихся чисел в исходной строке нет, программа ничего не должна выводить.


seq = [int(i) for i in input().split()]



counts = {}

for num in seq:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

duplicated_nums = [num for num, count in counts.items() if count > 1]
duplicated_nums.sort()

print(*duplicated_nums)