# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = self.income_dict

    income_dict = {"wage": None, "bonus": None}


class Position(Worker):
    income_dict = {"wage": 34780, "bonus": None}

    def get_full_name(self):
        print(f"\n\033[34mПозиция {self.position}:\n\033[0m\033[33mИмя: \033[36m{self.name},"
              f" \033[33mФамиллия: \033[36m{self.surname}\n")

    def total_income(self):
        wage = 0 if self._income["wage"] is None else self._income["wage"]
        bonus = 0 if self._income["bonus"] is None else self._income["bonus"]
        print(f"\033[31mоклад: {wage} руб, премия: {bonus} руб.\033[0m")


# print(Worker.income_dict)

position = Position("Антон", "Заглушкин", "разнорабочий")
# print(position) # экземпляр класса
position.get_full_name()
position.total_income()
