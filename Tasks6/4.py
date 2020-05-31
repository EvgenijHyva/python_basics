# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
from random import choice
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color}-car {self.name} is departed")

    def stop(self):
        print(f"{self.color}-car {self.name} is stopped")

    def turn(self, direction):
        if self.is_police:
            direction = ["\033[41mleft\033[0m", "\033[41mright\033[0m", "\033[41mstrait\033[0m",
                         "\033[41mTo-Berlin\033[0m", "\033[41mSan-francisco\033[0m"]
            print(f"{self.color}-car {self.name} is turning {choice(direction)}")
        else:
            print(f"{self.color}-car {self.name} is turning {direction}")


class TownCar(Car):
    print("\033[34mTownCar:\033[0m")

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} speed is \033[31m{self.speed}km\033[0m")
            print(f"\033[32mWarning!\033[0m Your speed is exceeded at \033[31m{self.speed - 60}km\033[0m")
        else:
            print(f"\033[36m{self.name} speed is {self.speed}km")


towncar = TownCar(65, "red", "citroen")
towncar.show_speed()
towncar.turn("left")


class SportCar(Car):
    print("\033[34mSportCar:\033[0m")

    def show_speed(self):
        print(f"{self.name} speed is \033[34m{self.speed}km\033[0m")


sportcar = SportCar(150, "Colorfull", "Camaro")
sportcar.go()
sportcar.show_speed()
sportcar.turn("right")


class WorkCar(Car):
    print("\033[34mWorkCar:\033[0m")

    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} speed is \033[31m{self.speed}\033[0m")
            print(f"\033[32mWarning!\033[0m Your speed is exceeded at \033[31m{self.speed - 40}km\033[0m")
        else:
            print(f"\033[36m {self.name} speed is {self.speed}km")


workcar = WorkCar(50, "blue", "Crane")
workcar.go()
workcar.show_speed()
workcar.stop()
print(workcar.is_police)


class PoliceCar(Car):
    print("\033[34mPoliceCar:\033[0m")

    def show_speed(self):
        print(f"{self.name} speed is \033[34m{self.speed}km\033[0m")


police = PoliceCar(70, "White", "Ford", True)
print(police.is_police)
police.go()
police.show_speed()
police.turn("left")
