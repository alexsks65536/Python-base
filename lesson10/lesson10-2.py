from abc import ABC, abstractmethod


class Clothes(ABC):
    output = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def calculation(self):
        pass

    def __add__(self, other):
        Clothes.output += self.calculation + other.calculation
        return Costume(0)

    def __str__(self):
        d = Clothes.output
        Clothes.output = 0
        return f"{d}"


class Coat(Clothes):
    @property
    def calculation(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def calculation(self):
        return round((2 * self.param + 0.3) / 100)


coat = Coat(52)
costume = Costume(180)
print(costume + coat + costume)