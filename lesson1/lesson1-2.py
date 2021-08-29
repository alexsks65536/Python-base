def summa(number): # функция возвращает сумму цифр числа number
    num = number
    sum = 0
    i = 0
    while i <= len(str(number)):
        sum = sum + num % 10
        num = num // 10
        i += 1
    return sum
row_cube = [] # список, состоящий из кубов нечётных чисел от 0 до 1000
for num in range(1, 1000):
    if num % 2 != 0:
        row_cube.append(num ** 3)
print("Список, состоящий из кубов нечётных чисел от 0 до 1000: \n", row_cube, "\nДлина списка = ", len(row_cube))
sum_cube_7 = 0 # сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
sum_cube_17 = 0 # К каждому элементу списка добавить 17 и заново вычислить сумму списка sum_cube
i = 0
while i <= len(row_cube) - 1:
    if summa(row_cube[i]) % 7 == 0:
        sum_cube_7 += row_cube[i]
    s = row_cube[i] + 17
    if summa(s) % 7 == 0:
        sum_cube_17 += s
    i += 1
print("Сумма списка, цифры которого делятся нацело на 7 = ", sum_cube_7)
print("Сумма списка, каждый элемент которого увеличен на 17 и делится нацело на 7 = ", sum_cube_17)


