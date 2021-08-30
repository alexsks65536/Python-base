class Number:

    def __init__(self, num):
        self.num = num

    @classmethod
    def get_num(cls):
        list = []
        while True:
            get_Number = input('Введите число,  "stop - выход: ')  # Ввод числа
            if get_Number == 'stop':
                return list
            elif get_Number.isalpha():
                get_Number = input('Нужно ввести число!: ')
            elif get_Number.isdigit():
                list.append(get_Number)


n = Number.get_num()
print(n)