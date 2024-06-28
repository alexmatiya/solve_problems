# Леа изучает программирование на Python и работает над учебным проектом — приложением для управления задачами
# (таск-менеджером). Ей пришло в голову дать пользователю возможность задавать теги при создании экземпляров.
# Со-ответственно, ей понадобилось добавить аргумент tags в метод __init__ (см. листинг 8.3).
# Она предполагает, что в большинстве случаев в аргументе tagsбудет передаваться
# пустой список. Какое значение по умолчанию ей следует назначить для tags в этом случае?


class Task:
    def __init__(self, title, desc, tags=None, urgency=1):
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.tags = [] if tags is None else tags


task = Task(title="Task 1", desc="Task description", tags=["tag1", "tag2"])
print(task.__dict__)

task2 = Task(title="Task 2", desc="Task description2", urgency=2)
print(task2.__dict__)
