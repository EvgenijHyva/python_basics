# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий
# подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора @property.
from abc import abstractmethod, ABC


class MyClothes(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def height(self):
        pass


class Suit(MyClothes):
    def __init__(self, H, color="Black"):
        super().__init__()
        self.suit_size = H
        self.color = color

    def __str__(self):
        return f"{self.color} Suit size {self.suit_size}"

    def size(self):
        pass

    def height(self):
        result = 2 * self.suit_size + 0.3
        print(f"{self.color}-cloth consumption for suit is: ")
        return round(result, 2)


class Coat(MyClothes):
    def __init__(self, V, color="Gray"):
        super().__init__()
        self.coat_size = V
        self.color = color

    def __str__(self):
        return f"{self.color} Coat size {self.coat_size}"

    def size(self):
        result = self.coat_size / 6.5 + 0.5
        print(f"{self.color}-cloth consumption for Coat is:")
        return round(result, 2)

    def height(self):
        pass


suit = Suit(48)
print(suit)
print(suit.height())

coat = Coat(152)
print(coat)
print(coat.size())
