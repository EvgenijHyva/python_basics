# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Date:
    def __init__(self, date_str):
        self.date = date_str

    def __str__(self):
        return f"User date is {self.date}"

    @classmethod
    def extract(cls, dat):
        char = "".join([i for i in "-,.:;/" if i in Date(dat).date])
        d = list(map(int, Date(dat).date.split(char)))
        print(f"Day - {d[0]}\nMonth - {d[1]}\nYear - {d[2]}")
        # print(type(d[0]),type(d[1]),type(d[2])) # проверка типов

    @staticmethod
    def valid(user_date):
        chart_list = ["-", ",", ".", ":", ";", "/"]
        try:
            for i in chart_list:
                if i in user_date:
                    user_date = user_date.split(i)
            user_date = list(map(int, user_date))
        except ValueError as err:
            print(f"\033[31m{err}\033[0m", "\nDate not valid, use separator('-','.',',',';',"
                                           "'/') example: dd-mm-yyyy or dd-mm-yy")
        else:
            if 31 >= user_date[0] > 1 and 12 >= user_date[1] and (9999 >= user_date[2] >= 0 or
                                                                  100 >= user_date[2] >= 0):
                print("\033[33mDate is valid\033[0m")
            else:
                print("\033[31mDate not valid, example: dd-mm-yyyy or dd-mm-yy\033[0m")

date = Date("12-05-2019")
Date.valid("15-15-2000")
Date.valid("12-5-2014")
Date.extract("12.03.2017")
Date.valid(input(f"\033[33mEnter date in format dd-mm-yyyy or dd-mm-yy\033[0m\n"))

