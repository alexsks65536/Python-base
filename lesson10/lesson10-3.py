class Cell:
    def __init__(self, number):
        self.number = number

    def make_order(self, set):
        return '\n'.join(['*' * set for _ in range(self.number // set)]) + '\n' + '*' * (self.number % set)

    def __str__(self):
        return f"{self.number}"

    def __mul__(self, other):
        print("Умножение клеток: ")
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        print("Деление клеток: ")
        return Cell(self.number // other.number)

    def __add__(self, other):
        print("Количество ячеек: ")
        return Cell(self.number + other.number)

    def __sub__(self, other):
        print("Разность ячеек: ")
        return Cell(self.number - other.number) if self.number - other.number > 0 \
            else "Вычитание невозможно. Ячеек в первой клетке меньше чем во второй"



cell_1 = Cell(241)
cell_2 = Cell(240)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(33))