# Функция get_date_range()
# Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:

# start — начальная дата, тип date
# end — конечная дата, тип date
# Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно. Если start > end, функция должна вернуть пустой список.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_date_range(), но не код, вызывающий ее.

# Примечание 2. Тестовые данные доступны по ссылкам:


from datetime import date, timedelta


def get_date_range(start, end):
    if start > end:
        return []

    date_range = []
    current_date = start

    while current_date <= end:
        date_range.append(current_date)
        current_date += timedelta(days=1)

    return date_range


if __name__ == "__main__":
    date1 = date(2021, 10, 1)
    date2 = date(2021, 10, 5)
    print(*get_date_range(date1, date2), sep="\n")

    date1 = date(2019, 6, 5)
    date2 = date(2019, 6, 5)

    print(get_date_range(date1, date2))
