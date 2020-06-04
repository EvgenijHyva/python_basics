# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран. Примеры строк файла: Информатика:   100(л)   50(пр)   20(
# лаб). Физика:   30(л)   —   10(лаб) Физкультура:   —   30(пр)   — Пример словаря: {“Информатика”: 170,
# “Физика”: 40, “Физкультура”: 30}
from googletrans import Translator

def read_line_by_line(file):
    """Lazy function generator, read file line by line"""
    while True:
        line = file.readline()
        if not line:
            break
        yield line

my_dict = {}

with open("text_6.txt") as file:
    content = read_line_by_line(file)
    for line in content:
        name, stats = line.split(":")
        name_sum = sum(map(int, "".join([i for i in stats if i == " " or ("0" <= i <= "9")]).split()))
        my_dict[name] = name_sum

print("\nрезультат сортировки файла:")
for k, v in my_dict.items():
    print(f"    предмет: {Translator().translate(k, dest='ru').text} = часы {v}")