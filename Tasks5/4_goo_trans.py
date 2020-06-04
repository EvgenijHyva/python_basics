# Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Необходимо
# написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
import googletrans as goo

# открытие файла на чтение:
data = open("text_4.txt", "r", encoding="utf-8")
content = data.readlines()
print(content)
for i in content:
    content[content.index(i)] = i.split()
data.close()

# запись в файл уже с транслитом
new_file = open("trans_text_4.txt", "a", encoding="utf-8")
for i in range(len(content)):
    result = goo.Translator().translate(content[i][0], dest="ru")  # перевод на русский
    print(result.text, content[i][2], sep=" - ", file=new_file)
new_file.close()
print("в файл 'trans_text_4.txt' записаны результары перевода")
