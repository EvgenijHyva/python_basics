# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
user_number = int(input("введите целое положительное число\n"))
a = user_number // 10
b = user_number % 10
if a > 9:
    while a > 9:
        if a > 9:
            c = a % 10
            if c > b:
                b = c
            a = a // 10
            if a < b <= 9:
                print("в числе {} самое большое: {}".format(user_number, b))
            elif b < a <= 9:
                print("в числе {} самое большое: {}".format(user_number, a))
elif a == 9 or b == 9:
    print(f"в числе {user_number} самое большое: 9")
