# Функция saturdays_between_two_dates()
# Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:

# start — начальная дата, тип date
# end — конечная дата, тип date
# Функция должна возвращать количество суббот между датами start и end включительно.

# Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию saturdays_between_two_dates(), но не код, вызывающий ее.

# Примечание 3. Тестовые данные доступны по ссылкам:

# Архив с тестами
# GitHub
# Sample Input 1:

# date1 = date(2021, 11, 1)
# date2 = date(2021, 11, 22)

# print(saturdays_between_two_dates(date1, date2))


from datetime import date, timedelta


def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start

    total_saturdays = 0
    current_date = start

    while current_date <= end:
        if current_date.weekday() == 5:  # 5 - Saturday
            total_saturdays += 1
        current_date += timedelta(days=1)

    return total_saturdays


if __name__ == "__main__":
    date1 = date(2021, 11, 1)
    date2 = date(2021, 11, 22)

    print(saturdays_between_two_dates(date1, date2))

    date1 = date(2020, 7, 26)
    date2 = date(2020, 7, 2)

    print(saturdays_between_two_dates(date1, date2))
