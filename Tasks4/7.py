# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове
# функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и
# до n!. Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4
# = 24.
from itertools import count
from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


gen = fact(15)  # проверка
print(gen)

for i in fact(15):
    print(i)


# __________________________________________________________________
def fact_gen():
    for i in count(1):
        yield factorial(i)


generator = fact_gen()
x = 0
for i in generator:
    if x == 15:
        break
    else:
        x += 1
        print(f"Factorial {x} = {i}")
