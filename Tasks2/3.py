# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.
seasons = ["зима", "весна", "лето", "осень"]
months = {
    1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август",
    9: "сентябрь", 10: "октябрь", 11: "Ноябрь", 12: "декабрь"
}
num_month = int(input("ведите номер месяца\n"))
while 12 < num_month or num_month == 0:
    num_month = int(input("максиму м 12 месяцев в году\n"))

if 9 <= num_month <= 11:
    print(seasons[3], ", месяц:", months[num_month])
elif 6 <= num_month <= 8:
    print(seasons[2], ", месяц:", months[num_month])
elif 3 <= num_month <= 5:
    print(seasons[1], ", месяц:", months[num_month])
else:
    print(seasons[0], ", месяц:", months[num_month])
