# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
# фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с
# фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}]. Итоговый список сохранить в виде json-объекта в соответствующий файл. Пример
# json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}] Подсказка: использовать
# менеджер контекста.
import codecs # для вывода русских букв в json
from json import dumps



def content_split(cont):
    """function splits content for a list"""
    try:
        for i in cont:
            cont[cont.index(i)] = i.split()
        return cont
    except TypeError:
        return TypeError, "открывать файл нужно file.readlines()!"


def get_firm_list(list_content):
    """function manipulate with listed content and returns List"""
    my_list = []
    firms_val = {}
    los_dict = {}
    for i in content:
        if int(i[2]) < int(i[3]):
            los_dict[i[0] + " " + i[1]] = int(i[2]) - int(i[3])
        firms_val[i[0] + " " + i[1]] = int(i[2]) - int(i[3])
    my_list.append(firms_val)
    aver_prof = (sum(firms_val.values()) - sum(los_dict.values())) / (len(firms_val) - len(los_dict))
    my_list.append({"average_profit": aver_prof})
    return my_list


with open("text_7.txt", "r", encoding="utf-8") as file:
    content = content_split(file.readlines())

# сериализация в json:
data = get_firm_list(content)

with codecs.open("new_json_file.json", "w", encoding="utf-8") as j_file:
    print(dumps(data, indent=4, ensure_ascii=False), file=j_file)
print("в документе 'new_json_file.json' добавлена запись")

