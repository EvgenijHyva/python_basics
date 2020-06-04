# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг —
# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода
# __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
# быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, matrix):
        self.list = matrix

    def __str__(self):
        string = "".join([str(i) for i in self.list]).replace(",", " ").replace("]", "\n").replace("[", " ")
        return string

    def __add__(self, other):
        new_mat = []
        if len(self.list) == len(other.list):
            for index, part in enumerate(self.list):
                new_obj = []
                for i in range(len(part)):
                    new_obj.append(self.list[index][i] + other.list[index][i])
                new_mat.append(new_obj)
            new_mat = "".join([str(i) for i in new_mat]).replace(",", " ").replace("]", "\n").replace("[", " ")
            return new_mat
        else:
            raise ValueError("Разно-размерные матрицы!")


matrix1 = [[2, 4, 6],
         [2, 5, 9],
         [3, 6, 8]]

matrix2 = [[5, 1, 0],
         [4, 8, 7],
         [2, 3, 6]]

mat1 = Matrix(matrix1)
mat2 = Matrix(matrix2)
print(mat1)
print(mat2)
print(mat1 + mat2)
