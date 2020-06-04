# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def div_func(num1, num2):  # позиционные аргументы : num1, num2
    try:
        result = float(num1) / float(num2)
    except ZeroDivisionError as err:
        print("на ноль делить нельзя как бэ, ошибка: %s" % err)
    else:
        print("готово")
        return result


print(div_func(input("делимое\n"), input("делитель\n")))
