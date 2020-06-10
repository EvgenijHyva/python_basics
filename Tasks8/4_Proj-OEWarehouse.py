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
    def __init__(self, height=10, size=100):
        self.size = {"Cub-m": size}
        self.height = {"m": height}
        self.__store_area_const = size
        self._equipment_list = []
        self.__not_fit_equipment = []

    def to_receive(self, *equipments):
        for equip in equipments:
            atr = equip.to_send()
            print(f"Required space for equip {atr[1].get('Cub-m')} Cub-m")
            # check for space in Warehouse
            if round(self.size['Cub-m']) > atr[1].get("Cub-m") > 0:
                self.size["Cub-m"] -= atr[1].get("Cub-m")  # Warehouse place deduction
                self._equipment_list.append(atr[0])
                print(f"{g}Equip added successfully at Warehouse{nc}")
                print(f"{nc if round(self.size['Cub-m'] / self.__store_area_const * 100) > 15 else r}Free space at "
                      f"warehouse:", round(self.size['Cub-m'] / self.__store_area_const * 100), "%")
            else:
                self.__not_fit_equipment.append(atr[0])
                print(f"More space required, at list: {atr[1].get('Cub-m') - round(self.size['Cub-m'])} Cub-m"
                      f"\nAdded to stack list: {atr[0][0]['equip']} - {atr[0][2]['type']}")
        if len(self.__not_fit_equipment) > 0:
            print(f"No space in Warehouse!Equipment in stack:\n{r}{self.not_fit_equip}{nc}")

    def show_wh_equip(self):
        for i in enumerate(self._equipment_list):
            print(f"{g}Active {i[0]}:  {b}{i[1][0]['equip']}-{i[1][2]['type']} ({i[1][1]['color']}) | "
                  f"{g}amount:{i[1][3]['qua']}{nc}")

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


oq = OfficeEquipment("scan", "xz+1", "3-f")
xe = Xerox("Canon", "Black", "24-xer")
sca = Scanner("Samsung", "CZ-50")
pri = Printer("SAMSUNG PRO", "Purple", "XC-19IE", 3)
pri1 = Printer("Samu", "green", "xT", 4)


# print("objects:", xe, oq, sca, pri)

# print(oew)

oew = OfficeEquipmentWarehouse(10, 50)
print(oew)
oew.to_receive(xe, xe, sca, pri, pri, xe, pri1, pri, xe)
oew.show_wh_equip()
class Client:
    printers = ["samsung", "Fast-P", "china-print", "Office-Print"]
    type_print = ["back-print", "color-print"]
    xeroxes = ["Canon", "Fast-Xerox", "Office-xerox"]
    type_xerox = ["UF-1", "Office-5", "ZX-black edition"]
    scanners = ["Just scanner", "Print and Scan"]
    type_scanners = ["Simple", "Personalized", "With-print", "Office-economy"]
    color = ["Back", "White", "Purple", "Colorful"]

    @staticmethod
    def new_warehouse():
        """If you wish you can create new ware house by this method
        split the warehouse dimensions(height and volume) with a comma"""

        user = input("create new Warehouse? Write height (m), write volume (Cub-m)."
                                   "For default size press enter. Default size = 100 Cub-m 10m height\n")
        try:
            user = list(map(int, user.split(",")))
        except ValueError:
            print("default is selected")

        if 3 > len(user) > 1:
            height, size = user
            print(height, size)
            if int(height) and int(size):
                oew = OfficeEquipmentWarehouse(height, size)
                return oew
        else:
            oew = OfficeEquipmentWarehouse()
            return oew

    quest = ["Select: Printers - 1, Xerox - 2, Scanner - 3. enter to exit\n",
             "How many equipment you want to place in Warehouse? enter to exit\n"]

    def placing(self):
        user = input("Select: Printers - 1, Xerox - 2, Scanner - 3. enter to exit\n")
        user = int(user) if user.isdigit() and 4 > int(user) >= 0 else 0
        print(user, type(user))



#w = Client().new_warehouse() # for creating new warehouse
#print(w)
#Client().placing()