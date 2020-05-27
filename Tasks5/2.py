# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
file = open("file_2.txt", "r", encoding="utf-8")
content = file.readlines()
print("количество сток в файле", len(content), sep=" = ")
for i in range(len(content)):
    print("количество слов в строке {}".format(i+1), len(content[i].split()), sep=" = ")
file.close()
