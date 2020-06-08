# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexInt:
    def __init__(self, z):
        self.a = z[0]
        self.bi = z[1]

    def __str__(self):
        return f"\r\033[37mComplex numbers z: real part {self.a}, imaginary part {self.bi}\033[0m\n"

    def __add__(self, other):
        a = self.a + other.a  # real part
        # imaginary units:
        i_part1 = int("-" + ("1" if len(self.bi.replace("-", "")) == 1 else self.bi.replace("i", "").replace
        ("-", ""))) if "-" in self.bi else int("1" if len(self.bi.replace("-", "")) == 1 else self.bi.replace("i", ""))

        i_part2 = int("-" + ("1" if len(other.bi.replace("-", "")) == 1 else other.bi.replace("i", "").replace
        ("-", ""))) if "-" in other.bi else int("1" if len(
            other.bi.replace("-", "")) == 1 else other.bi.replace("i", ""))
        # sum of imaginary units:
        tot_i_part = i_part1 + i_part2
        return f"\033[33mComplex sum: z = {a} {str(tot_i_part)+'i' if tot_i_part !=0 else ''}\033[0m"

    def __mul__(self, other):
        real = self.a * other.a  # real part

        # imaginary units:
        i_part1 = int("-" + ("1" if len(self.bi.replace("-", "")) == 1 else self.bi.replace("i", "").replace
        ("-", ""))) if "-" in self.bi else int("1" if len(self.bi.replace("-", "")) == 1 else self.bi.replace("i", ""))

        i_part2 = int("-" + ("1" if len(other.bi.replace("-", "")) == 1 else other.bi.replace("i", "").replace
        ("-", ""))) if "-" in other.bi else int("1" if len(
            other.bi.replace("-", "")) == 1 else other.bi.replace("i", ""))
        # sum of imaginary units:
        tot_i_part = other.a * i_part1 + self.a * i_part2

        imag_to_real = i_part1 * i_part2 * (-1)  # imaginary part to rea:i^2 = -1
        return f"\033[35mComplex numbers multiplication result:\n{real + imag_to_real} {tot_i_part}i\033[0m"


z1 = (3, "2i")
z2 = (2, "-3i")
z = ComplexInt(z1)
zz = ComplexInt(z2)
print(z, zz)
print(z + zz)
print(z * zz)
z1 = (3, "i")
z2 = (2, "-3i")
z = ComplexInt(z1)
zz = ComplexInt(z2)
print(z + zz)
print(z * zz)
z1 = (3, "3i")
z2 = (2, "-3i")
z = ComplexInt(z1)
zz = ComplexInt(z2)
print(z + zz)
print(z * zz)