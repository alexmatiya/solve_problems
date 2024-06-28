# 3.1.4. Задача page 93
# Зоя работает в компании, занимающейся разработкой картографических при-ложений. Она создает приложение, работающее
# с географическими точками. Для каждой точки хранится название, описание и координаты (широта и долгота).
# Какой контейнер использовать для хранения серии точек, посещенных пользо-вателем, — список или кортеж?
# Для каждой точки ей также понадобится модель данных для хранения координат. Где лучше хранить широту и долготу —
# в списке или в кортеже?
# ПОДСКАЗКА Подумайте, являются ли хранимые данные изменяемыми
# и/или однородными, — это поможет вам в принятии решения.




# 1. Для хранения серии точек, посещенных пользователем, следует использовать список (list),
# так как он является изменяемым контейнером, и пользователь может добавлять или удалять точки.

# 2. Для хранения координат (широты и долготы) каждой точки, следует использовать кортеж (tuple),
# так как координаты являются неизменяемыми и однородными данными.

# Таким образом, структура данных может выглядеть следующим образом:


# Список точек, посещенных пользователем
visited_points = [
    ("Point 1", "Description 1", (37.7749, -122.4194)),
    ("Point 2", "Description 2", (48.8566, 2.3522)),
    ("Point 3", "Description 3", (51.5074, -0.1278)),
]

# В этом примере visited_points является списком, где каждый элемент представляет собой кортеж,
# содержащий название, описание и координаты (широта, долгота) для каждой точки.
