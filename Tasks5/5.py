# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.
from itertools import islice, count
from random import randint
num_list = [randint(1, 100) for num in islice(count(15), 177) if num % 14 == 0 or num // 7 == 7]
print(num_list)
new_file = open("new_file.txt", "a+", encoding="utf-8")
for i in num_list:
    print(i, end=" ", file=new_file)
new_file.close()

new_file = open("new_file.txt", "r", encoding="utf-8")
content = new_file.readlines()
sums = 0
for i in content:
    content = i.split()
for i in range(len(content)):
    content[i] = int(content[i])
print("\nсумма чисел в файле", sum(content), sep=" : ")
new_file.close()
