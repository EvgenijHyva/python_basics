# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий
# подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора @property.
from abc import abstractmethod, ABC


class MyAbstractClass(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Clothes(MyAbstractClass):
    def __init__(self, param = 100):
        self.param = param
    @property
    def consumption_Coat(self, param):
        pass
    @property
    def consumption_Costume(self, param):
        pass
    @property
    def consumption(self):
        return self.consumption_Costume + self.consumption_Coat


class Costume(Clothes):

    def __str__(self):
        return f"Suit height {self.param}"

    @property
    def consumption(self):
        result = round(2 * self.param + 0.3, 2)
        Clothes.consumption_Costume = result
        return f"Cloth consumption for Costume height {self.param}  is {result}"


class Coat(Clothes):
    def __str__(self):
        return f"Coat size {self.param}"

    @property
    def consumption(self):
        result = round(self.param / 6.5 + 0.5, 2)
        Clothes.consumption_Coat = result
        return f"Cloth consumption for Coat {self.param} size is {result}"

m1 = Clothes()
m2 = Coat(35)
print(m2.consumption)
m3 = Costume(178)
print(m3.consumption)
print(f"Total cloth consumption = {m1.consumption}")