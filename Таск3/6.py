# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В
# программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
# регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().
def int_func(some_text: str):
    """
    Function input: text. Function overwrite words with capitalized first letter.
    :param some_text: text, it should be space separated
    :return: word with Capitalised first letter.
    """
    some_text: list = some_text.split()
    suggestion = ""
    for word in some_text:
        word = word[:1].upper() + word[1:]
        suggestion += "".join(word) + " "
    return suggestion

# print(int_func(input("текст\n")))
# print(int_func("здЭсь находится текст длЯ проверки РаБоТы функции")) # -> проверка текста


