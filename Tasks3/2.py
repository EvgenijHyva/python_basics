# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def pers_func(name, surname, year_of_birth, city, email, phone):
    email = None if email.count("@") == 0 else email
    print(f"Имя - {name}; фамилия - {surname}; год рождения - {year_of_birth}; город проживания -{city},"
          f"email - {email}, телефон - {phone}")


pers_info = ["Имя\n", "фамилия\n", "год рождения\n", "город проживания\n", "email\n", "телефон\n"]
for i in range(len(pers_info)):
    pers_info[i] = input(pers_info[i])
name, surname, year_of_birth, city, email, phone = pers_info

pers_func(name, surname, year_of_birth, city, email, phone)
