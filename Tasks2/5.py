# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
# элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


my_raiting = [7, 5, 3, 3, 2]
print(my_raiting)
count = 0

while count < 20:
    if len(my_raiting) >= 6:
        my_raiting.pop()
    new_element = int(input("новый элемент рейтинга\n"))
    if new_element in my_raiting:
        index = my_raiting.index(new_element)
        my_raiting.insert(index + 1, new_element)
        print(my_raiting)
    else:
        for i in my_raiting:
            if new_element > i:
                my_raiting.insert(my_raiting.index(i), new_element)
                print(my_raiting)
                break
        if new_element not in my_raiting:
            my_raiting.append(new_element)
            print(my_raiting)
    count += 1
