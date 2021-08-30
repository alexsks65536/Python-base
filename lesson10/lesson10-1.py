
class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])

        return '\n'.join(map(str, c))

matrix_1 = Matrix([[1, 2, 8], [3, 4, 6], [5, 6, -3]])
matrix_2 = Matrix([[1, 0, 0], [2, 0, -6], [3, 0, -1]])

print(f"Matrix_1:\n{matrix_1}")
print(f"Matrix_2:\n{matrix_2}")
print(f"Matrix_1 + Matrix_2\n{matrix_1 + matrix_2}")