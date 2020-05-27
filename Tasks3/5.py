# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

num_list = []
copy_list = []
result = 0
cycle = True
sum = 0
while cycle:
    numbers = input("введите числа разделяя их пробелом. спец символ для вывода суммы $\n")
    numbers = numbers.split()
    print(numbers)
    if "$" in numbers:
        if "$" in numbers and len(numbers) > 1:
            if numbers.count("$") > 0:
                numbers.pop(numbers.index("$"))
                for i in range(len(numbers)):
                    result += int(numbers[i])
                copy_list += numbers
                numbers.clear()
                cycle = False
        else:
            cycle = False
    else:
        num_list += numbers
        copy_list += num_list
        for i in range(len(num_list)):
            sum += int(numbers[i])
            num_list.clear()
    sum += result
    print(f"сумма чисел: {sum}")
print(f"счет закончен, введенные числа: {copy_list}")
