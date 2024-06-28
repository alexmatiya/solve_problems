# 6.1.5. Задача page 198
# Кори преподает программирование на Python в колледже. Он хочет показать
# сту-дентам, что аргументы по умолчанию
# вычисляются при определении функции, а не при ее вызове. Как бы вы
# предложили ему подкрепить это утверждение?
# ПОДСКАЗКА Создайте временную метку для проверки того, что происходит
# во время определения и вызовов функции. Следующий фрагмент позволяет
# получить временную метку:
# from datetime import datetimetimestamp = datetime.today()
import time
from datetime import datetime


def print_time(time_arg=datetime.now()):
    print(f"Time at function definition: {datetime.now()}")
    print(f"Time at function call: {time_arg}")
    print("")


print_time()
time.sleep(1)
print_time()
print_time()
