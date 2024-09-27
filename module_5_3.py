class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def go_to(self, new_floor: int):
        inter_num = range(1, self.number_of_floors + 1)
        if new_floor in inter_num:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return 'Неверный класс объекта. Для корректной работы метода представьте объект класса House'
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return 'Неверный класс объекта. Для корректной работы метода представьте объект класса House'
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return 'Неверный класс объекта. Для корректной работы метода представьте объект класса House'
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return 'Неверный класс объекта. Для корректной работы метода представьте объект класса House'
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return 'Неверный класс объекта. Для корректной работы метода представьте объект класса House'
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return 'Неверный класс объекта. Для корректной работы метода представьте объект класса House'

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            print('Неверный класс объекта. Для корректной работы метода представьте объект класса Int')
            return self
    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            print('Неверный класс объекта. Для корректной работы метода представьте объект класса Int')
            return self
    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            print('Неверный класс объекта. Для корректной работы метода представьте объект класса Int')
            return self

    def __sub__(self, other):
        if isinstance(other, int):
            self.number_of_floors -= other
            return self
        else:
            print('Неверный класс объекта. Для корректной работы метода представьте объект класса Int')
            return self
    def __mul__(self, other):
        if isinstance(other, int):
            self.number_of_floors = int(self.number_of_floors * other)
            return self
        else:
            print('Неверный класс объекта. Для корректной работы метода представьте объект класса Int')
            return self
    def __floordiv__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors // other
            return self
        else:
            print('Неверный класс объекта. Для корректной работы метода представьте объект класса Int')
            return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

h1 = h1 * h2
h2 = h2 // 5

print(h1, h2, sep='\n')

h1 = h1 - 5
print(h1)