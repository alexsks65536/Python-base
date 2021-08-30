class Store:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        ''' заносим в словарь обьекты по названию, в значении
        будет список экземпляров этого оборудования '''
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        ''' извлекаем из значения обьект по названию группы.
        дальше можно расширить поиск по серии, марки или еще чему либо'''
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, made_in, year):
        self.name = name
        self.made_in = made_in
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.made_in} {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, made_in, year):
        super().__init__(name, made_in, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.made_in} {self.year}'

    def action(self):
        return 'Печатает'


class Scanner(Equipment):
    def __init__(self, name, made_in, year):
        super().__init__(name, made_in, year)

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, made_in, year):
        super().__init__(name, made_in, year)

    def action(self):
        return 'Копирует'


store = Store()
# создаем объект и добавляем
scanner = Scanner('epson', '168', 120)
store.add_to(scanner)
scanner = Scanner('Unix', '123', 85)
store.add_to(scanner)
xerox = Xerox('Canon', '1698', 1234)
store.add_to(xerox)
printer = Printer('M2540dn', 'Kyocera', 260, 2021)
store.add_to(printer)
# выводим склад
print(store._dict)
# забираем с склада и выводим склад
store.extract('Scanner')
print()
print(store._dict)

