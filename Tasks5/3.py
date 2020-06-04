# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
# подсчет средней величины дохода сотрудников. Пример файла: Иванов 23543.12 Петров 13749.32
data = open("text_3.txt", "r", encoding="utf-8")
content = data.readlines()
surname_dict = {}
check_salary = 20000.0  # переменная анализа зарплат сотрудников
salary_sum = 0
for line in content:
    name_list = tuple(line.split())
    salary_sum += float(name_list[1])
    for i in range(len(name_list) - 1):
        if float(name_list[i + 1]) < check_salary:  # вывод фамили сотрудников с зарплатой меньше 20000
            surname_dict[name_list[i]] = float(name_list[i + 1])
data.close()

print("\nкороткий анализ:")
print("средний оклад сотрудников: %.2f\n" % (salary_sum/len(content)))
print("список сотрудников с окладом меньше {}:".format(check_salary))
for i, k in surname_dict.items():
    print(f"{i} - {k}")
