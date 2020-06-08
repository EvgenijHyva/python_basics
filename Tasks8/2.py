# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class MyException(Exception):
    def __init__(self, txt, num):
        self.txt = txt
        self.num = num


def divide(a, b):
    try:
        if b == 0:
            raise MyException("Occurred exception, divider:", b)
        res = a / b
    except MyException as err:
        return f"Zero divide not allowed {err}"
    else:
        return res


print(divide(10, 0))
