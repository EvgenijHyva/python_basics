# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.

def my_func(arg1, arg2, arg3):
    """Arguments should be numbers for function correct functionality"""
    my_list = [int(arg1), int(arg2), int(arg3)]
    my_list.pop(my_list.index(min(my_list)))
    res = sum(my_list)
    return res


print(my_func(input("arg1"), input("arg2"), input("arg3")))
