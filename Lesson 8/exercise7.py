class ComplexNumber:
    number: complex

    def __init__(self, real, imag):
        self.number = complex(real, imag)

    @classmethod
    def from_complex(cls, complex: complex):
        return cls(complex.real, complex.imag)

    def __add__(self, other):
        return ComplexNumber.from_complex(self.number + other.number)

    def __mul__(self, other):
        return ComplexNumber.from_complex(self.number * other.number)

    def __str__(self):
        return str(self.number)

    def print(self):
        print(self.number)


num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(3, 4)

num3 = num1 + num2
num4 = num1 * num2
print(num3.number)
print(num4.number)

print(f'Проверка. {num1}+{num2} = {complex(1, 2) + complex(3, 4)}')
print(f'Проверка. {num1}*{num2} = {complex(1, 2) * complex(3, 4)}')
