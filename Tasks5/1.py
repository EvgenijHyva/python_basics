# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.

file = open("file_1.txt", "w", encoding="utf-8")
file.write(input("введите информацию\n"))
file.close()