# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.
from sys import argv


def salary_calc(filtered_list):
    """Calculate salary by formula. func takes list of numbers"""
    try:
        result = filtered_list[0] * filtered_list[1] + filtered_list[-1]
        return round(result, 2)
    except TypeError:
        return "Проверь аргументы"


def float_filter(func_list):
    """function filters argv-input to float-values"""
    try:
        for word in (func_list):
            for i in word:
                if "," in i:
                    index = func_list.index(word)
                    num = func_list.pop(index).replace(",", ".")
                    func_list.insert(index, num)
        for i in range(len(func_list)):
            func_list[i] = float(func_list[i])
        return func_list
    except ValueError:
        print("Расчет производится только цифрами")
        
try:
    name, hours, rate, bonus = argv
    func_list = [hours, rate, bonus]
    print("название скрипта", name, sep=":")
    print(salary_calc(float_filter(func_list)))
except ValueError:
    print("Укажите 3 аргумента для расчета")
