# 8.5.6. Задача page 298
# В разделе 8.1 вы узнали, как реализовать метод __init__ в пользовательском классе. Если подкласс содержит такую
# же реализацию, как надкласс, переопре-делять __init__ вообще не придется. Но если вам нужна специальная
# иници-ализация, как в случае Supervisor, необходимо переопределить __init__. Как переопределить __init__ в
# классе Supervisor?
# ПОДСКАЗКА Переопределение __init__ не отличается от переопределения других методов. Вызов super() используется
# для создания объекта-замести-теля, через который будет вызываться конструктор надкласса.


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id


class Supervisor(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary


supervisor = Supervisor("John Doe", 45, 84)
print(supervisor.name)
print(supervisor.employee_id)
print(supervisor.salary)
print(supervisor.__class__.__mro__)
