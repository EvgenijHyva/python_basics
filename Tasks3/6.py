# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В
# программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
# регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().
def latin_let_filter(text):
    """
    Function checks SMALL-latin-letters.
    :param text: small latin text
    :return: True or None
    """
    for word in text:
        for letter in word:
            if ord(letter) <= 96 or ord(letter) >= 123:
                print("small latin letters only!")
                print("word", word, sep=" -> ")
                return None
    return True


def int_func(some_text: str):
    """
    Function input: text. Function overwrite words with capitalized first letter.
    Function has a latin small-letter filter.
    :param some_text: text, it should be space separated
    :return: word with Capitalised first letter.
    """
    some_text = some_text.split()
    if latin_let_filter(some_text) is True:
        suggestion = ""
        for word in some_text:
            word = word[:1].upper() + word[1:]
            suggestion += "".join(word) + " "
        return suggestion
    return "function ends the execution"


print(int_func(input("текст маленькими латинскими буквами\n")))


# print(int_func("здЭсь"))  # -> проверка текста
# print(int_func("zdes nahoditSja teKst dlja proверки РаБоТы функции"))
# print(int_func("zdes nahoditSja teKst dlja prOverkI raboty funkcii"))  # -> проверка текста
# print(int_func("zdes "))

# ____________________________________________________________________________________________
def int_func_v2(some_text: str):
    """
    Function input: text. Function overwrite words with capitalized first letter.
    Function has a only latin-letter filter. When filter returns None, function
    ends the execution.

    :param some_text: text, it should be space separated
    :return: word with Capitalised first letter.
    """

    def func_filter(text):
        """
        Function checks big-small latin letters, numbers characters -> return True
        :param text: latin letters, characters, numbers, space
        :return: True or None
        """
        for word in text:
            for letter in word:
                if ord(letter) <= 30 or ord(letter) >= 170:
                    print("LATIN letters, numbers, characters only!")
                    print("Some random word", word, sep=" -> ")
                    return None
        return True

    some_text: list = some_text.split()
    if func_filter(some_text) is True:
        suggestion = ""
        for word in some_text:
            word = word[:1].upper() + word[1:]
            suggestion += "".join(word) + " "
        return suggestion
    return "function ends the execution"

print(int_func_v2(input("текст латинскими буквами, цифрами или с набором знаков\n")))
# print(int_func_v2("здЭсь находится текст длЯ проверки РаБоТы функции"))  # -> проверка текста
# print(int_func_v2("zdes nahoditSJA teKst dlJA proверки РаБоТы функции"))
# print(int_func_v2("zdEs nahoDitSJA teKst dlja prOverkI raBoTy funKciI"))  # -> проверка текста
