# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
# списка. Подсказка: использовать функцию reduce().
from functools import reduce
my_list = [num for num in range(100, 1001) if num % 2 == 0]


def my_func(var1, var2):
    """function for number production"""
    return var1 * var2


print(reduce(my_func, my_list))

# _____________________________________________________________________________________

print(reduce(lambda a, b: a*b, [x for x in range(100, 1001, 2)]))