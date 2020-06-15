# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа. Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток. Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
# если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение. Умножение.
# Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух
# клеток. Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток. В классе необходимо реализовать метод make_order(), принимающий экземпляр класса
# и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида
# *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда
# не хватает, то в последний ряд записываются все оставшиеся. Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**. Или, количество ячеек клетки
# равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****. Подсказка:
# подробный список операторов для перегрузки доступен по ссылке.
from math import floor


class Cell:
    def __init__(self, group):
        self.group = group

    def __str__(self):
        return f"Cells quantity is: \033[32m\033[1m{self.group}\033[0m"

    def __add__(self, other):
        self.group = self.group + other.group
        return f"Result of cells sum: \033[32m\033[1m{self.group}\033[0m"

    def __sub__(self, other):
        if self.group > other.group:
            self.group = self.group - other.group
            return f"Result of cells subtraction: \033[32m\033[1m{self.group}\033[0m"
        else:
            raise ValueError("can´t subtract! result < 0, that´s mean all cells are dead")

    def __mul__(self, other):
        self.group = self.group * other.group
        return f"Result of cells multiplying: \033[32m\033[1m{self.group}\033[0m"

    def __truediv__(self, other):
        self.group = round(self.group / other.group)
        return f"Result of cells dividing: \033[32m\033[1m{self.group}\033[0m"

    def make_order(self, num_el_in_row):
        res = ["".join("[\033[31mO\033[0m]") for i in range(self.group)]
        for i in range(floor(self.group / num_el_in_row)):
            res.pop((i + 1) * num_el_in_row - 1)
            res.insert((i + 1) * num_el_in_row - 1, "[\033[31mO\033[0m]\n")
        res = "".join(res)
        return f"Cells quantity in row: \033[31m\033[1m[{num_el_in_row}]\033[0m.\n" \
               f"Rows: [\033[36m\033[1m{round(self.group/num_el_in_row)}\033[0m] -> \n{res}\n\n" \
               f"Total cells value: \033[31m\033[1m[{self.group}]\033[0m "

        # альтернативный варик с генератором:
    #def make_order(self, num_el_in_row):
       # return "n".join(["*" * num_el_in_row for _ in range(self.group // num_el_in_row)])\
        #       + "\n" + "*" *(self.group % num_el_in_row)



cell = Cell(35)
cell2 = Cell(17)
#print(cell + cell2)
#print(cell / cell2)
#print(cell * cell2)
print(cell)
#print(cell - cell2)
print(cell.make_order(7))
