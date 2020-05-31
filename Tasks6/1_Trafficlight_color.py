# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу
# можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.
import time

#self.__red = "\033[1m\033[41m\033[30m"
#self.__yellow = "\033[1m\033[42m\033[30m"
#self.__green = "\033[1m\033[43m\033[30m"

class TrafficLight():
    def __init__(self):
        self.__red = "\033[41m| |\033[0m"
        self.__yellow = "\033[42m| |\033[0m"
        self.__green = "\033[43m| |\033[0m"
        print(f"инициализация светофора:\n{self.__red}\n{self.__yellow}\n{self.__green}")
        print("\033[0mсветофор работает, перезапуск\n\n\n")
        time.sleep(1)

    def running(self):
        count = 0
        while count < 10:
            print(self.__red + "{}".format("\033[1m\033[31m Red Light, Stay\033[0m"))
            time.sleep(7)
            print(self.__yellow + "{}".format("\033[1m\033[32m Yellow Light, wait - >green\033[0m"))
            time.sleep(2)
            print(self.__green + "{}".format("\033[1m\033[33m Green Light, now you can go\033[0m"))
            time.sleep(10)
            print(self.__yellow + "{}".format("\033[1m\033[32m Yellow Light, soon  turning to red\033[0m"))
            time.sleep(2)
            count += 1


trafficlight = TrafficLight()
print("запуск")
trafficlight.running()
