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
from random import choice

r, g, y, b, nc = ("\033[31m", "\033[32m", "\033[33m", "\033[35m", "\033[0m")  # coloring for output


class OfficeEquipmentWarehouse:
    def __init__(self, height=10, size=1000):
        self.size = {"Cub-m": size}
        self.height = {"m": height}
        self.__store_area_const = size
        self._equipment_list = []
        self.__not_fit_equipment = []

    def to_receive(self, *equipments):
        for equip in equipments:
            atr = equip.to_send()
            print(f"Required space for equip {round(atr[1].get('Cub-m'), 2)} Cub-m")
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
        return f"{r}{'list is empty' if not info else f'waiting for free place:{info}'} {nc}"

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


class Client:
    # Create list of equipment randomly:
    printers = ["samsung", "Fast-P", "china-print", "Office-Print"]
    type_print = ["back-print", "color-print"]
    xeroxes = ["Canon", "Fast-Xerox", "Office-xerox"]
    type_xerox = ["UF-1", "Office-5", "ZX-black edition"]
    scanners = ["Just scanner", "Print and Scan"]
    type_scanners = ["Simple", "Personalized", "With-print", "Office-economy"]
    color = ["Back", "White", "Purple", "Colorful"]
    equip = []

    @staticmethod
    def new_warehouse():
        """If you wish you can create new ware house by this method
        split the warehouse dimensions(height and volume) with a comma"""

        user = input("create new Warehouse? Write height (m), write volume (Cub-m)."
                     "For default size press enter. Default size = 1000 Cub-m 10m height\n")
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

    # under construction!
    def issue_wh(self, action):
        if action == "1":
            print("printer\n")
        elif action == "2":
            print("scanner\n")
        elif action == "3":
            print("xerox\n")
        else:
            print(f"{r}Only 1, 2, 3\n{nc}")

    def warehouse_action(self):
        global oew
        try:
            action = input(f"{g}New WH? y/n?{nc}\n")
            if action == "y":
                oew = Client().new_warehouse()
            else:
                oew = OfficeEquipmentWarehouse(10, 1000)
            while True:
                action = input(f"{g}Select operation:{nc}\n<1> Placing to warehouse\n<2> Issue from warehouse"
                               "\n<3> Warehouse inventorization\n<4> Awaiting loading at the warehouse\n"
                               f"<5> Clear order list\nOr <Enter> to exit\n")
                if action == "":
                    print("selected exit")
                    break
                elif action == "1":
                    action = input("What you want to place in warehouse?\n<1> printer\n<2> scanner\n<3> xerox\n")
                    if action == "":
                        break
                    elif action == "1":
                        act = input("quantity")
                        oew.to_receive(
                            Printer(choice(self.printers), choice(self.type_print), choice(self.color), int(act)))
                    elif action == "2":
                        act = input("quantity")
                        oew.to_receive(
                            Scanner(choice(self.scanners), choice(self.type_scanners), choice(self.color), int(act)))
                    elif action == "3":
                        act = input("quantity")
                        oew.to_receive(
                            Xerox(choice(self.xeroxes), choice(self.type_xerox), choice(self.color), int(act)))
                    else:
                        print("I dont know what you want")

                elif action == "2":
                    action = input("Select equip from warehouse:\n<1> Printer\n<2> Scanner\n<3> Xerox\n")
                    self.issue_wh(action)
                    print("under construction")

                elif action == "3":
                    print("checking warehouse:")
                    print(f"Warehouse storage value: {oew.storage} Cub-m")
                    oew.show_wh_equip()

                elif action == "4":
                    print(oew.not_fit_equip)

                elif action in "5":
                    print(oew.clean_not_fit_equip)
                # secret function:
                elif action == "666":
                    des = input(f"{r}Are you sure?It will destroy everything, and create new warehouse-word! y/n\n{nc}")
                    if des == "y":
                        oew = Client().new_warehouse()
                    elif des == "n":
                        print(f"{y}Okay i^ll give a chance for you{nc}")
                        continue
                    else:
                        continue

                else:
                    print("Selected unknown operation")
                    continue
        # exceptions:
        except TypeError as err:
            print("Write only numbers")
            with open("err-log.txt", "a", encoding="utf-8") as file:
                file.write(f"{err}\n")
        except ValueError as err:
            print("Write only numbers")
            with open("err-log.txt", "a", encoding="utf-8") as file:
                file.write(f"{err}\n")


Client().warehouse_action()
