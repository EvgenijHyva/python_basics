# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка. Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например,
# команду “stop”. При этом скрипт завершается, сформированный список выводится на экран. Подсказка: для данного
# задания примем, что пользователь может вводить только числа и строки. При вводе пользователем очередного элемента
# необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. Класс-исключение
# должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа
# скрипта не должна завершаться.
class MyException(Exception):
    def __init__(self, txt, *args):
        self.txt = txt
        self.char = args


def my_func():
    my_list = []
    stop = None
    while not stop:
        user = list(input("Enter integers or '$' for exit\n").split(","))
        # Check for Exception and stop-symbol generator-searchers:
        check, stop = [i for i in user if not i.isdigit() and i != "$"], [x for x in user if x == "$"]
        try:
            if check:
                raise MyException("Only numbers or '$'! You have entered:", check)
        except MyException as err:
            print(err)
        else:
            user = [int(i) for i in user if i.isdigit()]
            my_list += user
            if stop:
                print(f"\033[33mYour´s numbers list is \033[0m:\n{my_list},"
                      f"\n\033[33mList length: \033[0m{len(my_list)}")
                break


my_func()