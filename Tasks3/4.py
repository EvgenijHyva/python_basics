# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй —
# более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    """pow function x is number, y is exponent, function returns result"""
    try:
        if y < 0:
            return 1 / (abs(x) ** abs(y))
        elif y == 0:
            return 1
        else:
            return round(x ** y)
    except ZeroDivisionError as err:
        print("ноль не может возвестись в негативную степень : %s" % err)


try:
    print(my_func(float(input("число")), float(input("степень"))))
except ValueError as err:
    print("Ошибка в значениях : %s" % err)


# --------------------------------------------------------------------------------------------------
# решение 2:

def my_func2(x, y):
    """
    pow function version 2
    :param x: number
    :param y: exponent number
    :return: result
    """
    z = x
    for i in range(abs(y) - 1):
        x = x * z
    try:
        if y > 0:
            return x
        elif y == 0:
            return 1
        else:
            return 1 / x
    except ZeroDivisionError as err:
        print("ноль не может возвестись в негативную степень : %s" % err)


try:
    print(my_func2(int(input("число")), int(input("степень"))))
except ValueError as err:
    print("Ошибка в значениях : %s" % err)
