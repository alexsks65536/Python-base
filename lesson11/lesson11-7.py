class NumComplex:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, NumComplex):
            other = other.__complex

        complex_ = self.__complex + other
        return NumComplex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, NumComplex):
            other = other.__complex

        complex_ = self.__complex * other
        return NumComplex(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


if __name__ == '__main__':
    c1 = NumComplex(7, -5)
    c2 = NumComplex(3)

    print(c1 + c2, complex(4, -7) + complex(8))
    print(c1 * c2, complex(5, -8) * complex(2))
