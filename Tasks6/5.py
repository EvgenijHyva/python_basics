# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def drow(self):
        print("Start drawing")

class Pencil(Stationery):

    def drow(self):
        print(f"draw with a {self.title}")

class Pen(Stationery):

    def drow(self):
        print(f"draw with a {self.title}")

class Handle(Stationery):

    def drow(self):
        print(f"Star drawing with a {self.title}")


stationary = Stationery("School-box")
stationary.drow()
pen = Pen("Blue-pen")
pen.drow()
handle = Handle("Red-handle")
handle.drow()
pencil = Pencil("Gray pencil")
pencil.drow()