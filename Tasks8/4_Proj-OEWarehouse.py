# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о
# наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип
# данных. Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
r, g, y, b, nc = ("\033[31m", "\033[32m", "\033[33m", "\033[35m", "\033[0m")  # colloring for output


class OfficeEquipmentWarehouse:
    def __init__(self, size=100):
        self.size = {"Cub-m": size}
        self.height = {"m": 10}
        self.__store_area_const = size
        self._equipment_list = []
        self.__not_fit_equipment = []

    def to_receive(self, *equipments):
        for equip in equipments:
            atr = equip.to_send()
            print("required space for equip", atr[1].get("Cub-m"))
            # check for space in Warehouse
            if round(self.size['Cub-m']) > atr[1].get("Cub-m") > 0:
                self.size["Cub-m"] -= atr[1].get("Cub-m")  # Warehouse place deduction
                self._equipment_list.append(atr[0])
                print("Equip added")
                print("in class list", self._equipment_list)
                print("space:", round(self.size['Cub-m'] / self.__store_area_const * 100), "%")
            else:
                self.__not_fit_equipment.append(atr[0])
                print(f"More space required, at list: {atr[1].get('Cub-m') - round(self.size['Cub-m'])} Cub-m"
                      f"\nAdded to stack list: {atr[0][0]['equip']} - {atr[0][2]['type']}")
            input()
        if len(self.__not_fit_equipment) > 0:
            print(f"No space in Warehouse!Equipment in stack:\n{r}{self.not_fit_equip}{nc}")

    def __str__(self):
        return f"{g}Warehouse {round(self.size['Cub-m'], 2)}m^3 size, store area " \
               f"about {round(self.size['Cub-m'] / self.__store_area_const * 100)}%{nc}."

    @property
    def storage(self):
        return round(self.size["Cub-m"], 2)

    @property
    def not_fit_equip(self):
        info = []
        for i in enumerate(self.__not_fit_equipment):
            info.append([f"{i[1][0]['equip']} - {i[1][2]['type']}", i[1][3]['qua']])
        return f"{info}"

    @property
    def clean_not_fit_equip(self):
        self.__not_fit_equipment.clear()
        return f"{g}Stack list cleared{nc}"


class OfficeEquipment:
    def __init__(self, name, color, t, q=1):
        self.name = {"equip": name}, {"color": color}, {"type": t}, {"qua": q}
        self.place = {"Cub-m": 0}

    def __str__(self):
        return f"Equipment: {self.name[0]['equip']} {self.name[2]['type']} quantity: {self.name[3]['qua']}"

    def to_send(self):
        return self.name, self.place


class Printer(OfficeEquipment):
    def __init__(self, name, color, t, q=1):
        super().__init__(name, color, t, q)
        self.area = {"Sq-m": 2}
        self.height = {"m": 1.5}
        self.place = {"Cub-m": self.area["Sq-m"] * self.height["m"] * q}


class Xerox(OfficeEquipment):
    def __init__(self, name, color, t, q=1):
        super().__init__(name, color, t, q)
        self.area = {"Sq-m": 1.2}
        self.height = {"m": 0.8}
        self.place = {"Cub-m": self.area["Sq-m"] * self.height["m"] * q}


class Scanner(OfficeEquipment):
    def __init__(self, name, color, t="fast-scanner", q=1):
        super().__init__(name, color, t, q)
        self.area = {"Sq-m": 0.8}
        self.height = {"m": 0.5}
        self.place = {"Cub-m": self.area["Sq-m"] * self.height["m"] * q}


oew = OfficeEquipmentWarehouse(10)
oq = OfficeEquipment("scan", "xz+1", "3-f")
xe = Xerox("Canon", "Black", "24-xer")
sca = Scanner("Samsung", "CZ-50")
pri = Printer("SAMSUNG PRO", "Purple", "XC-19IE", 3)
pri1 = Printer("Samu", "green", "xT", 4)
# print(xe, oq, sca, pri)

oew.to_receive(xe, xe, sca, pri, pri, xe, pri1, pri, xe)

print(oew)

print(oew.clean_not_fit_equip)
