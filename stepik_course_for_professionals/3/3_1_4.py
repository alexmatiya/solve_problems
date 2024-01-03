# Вам доступен список dates, содержащий даты. Дополните приведенный ниже код, чтобы он вывел год и номер квартала каждой даты из данного списка. Компоненты дат должны быть расположены в исходном порядке, каждые на отдельной строке, в следующем формате:

# <год>-Q<номер квартала>
# Примечание 1. Продолжительность кварталов:

# 1
# 1 квартал	январь, февраль, март
# 2
# 2 квартал	апрель, май, июнь
# 3
# 3 квартал	июль, август, сентябрь
# 4
# 4 квартал	октябрь, ноябрь, декабрь
# Примечание 2. Начальная часть ответа выглядит так:

# 2010-Q3
# 2017-Q1

from datetime import date

dates = [
    date(2010, 9, 28),
    date(2017, 1, 13),
    date(2009, 12, 25),
    date(2010, 2, 27),
    date(2021, 10, 11),
    date(2020, 3, 13),
    date(2000, 7, 7),
    date(1999, 4, 14),
    date(1789, 11, 19),
    date(2013, 8, 21),
    date(1666, 6, 6),
    date(1968, 5, 26),
]

for day in dates:
    if day.month in [1, 2, 3]:
        print(f"{day.year}-Q1")
    elif day.month in [4, 5, 6]:
        print(f"{day.year}-Q2")
    elif day.month in [7, 8, 9]:
        print(f"{day.year}-Q3")
    elif day.month in [10, 11, 12]:
        print(f"{day.year}-Q4")
