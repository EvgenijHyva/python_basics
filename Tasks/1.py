# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

# калькулятор:

while True:
    operation = input("выберете операцию: *, /, +, -, %, //, **, exit-для выхода\n")
    if operation == "exit":
        print("выход")
        break

    a = int(input("введите число а\n"))
    b = int(input("введите число б\n"))

    if operation == "*":
        print(a * b)
    elif operation == "/":
        print(a / b)
    elif operation == "-":
        print(a - b)
    elif operation == "+":
        print(a + b)
    elif operation == "%":
        print(a % b)
    elif operation == "//":
        print(a // b)
    elif operation == "**":
        print(a ** b)
    else:
        print("повторите, выбрана неправильаня операция")
        continue
