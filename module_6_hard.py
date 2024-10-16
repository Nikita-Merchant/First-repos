import math

class Figure:
    sides_count = 0
    def __init__(self, color, *sides, filled=True):
        if isinstance(self, Cube):
            if len(sides) == 1:
                self.__sides = [sides[0] for _ in range(12)]
            else:
                self.__sides = [1 for _ in range(12)]
        else:
            if len(sides) == self.sides_count:
                list_ = []
                for side_1 in sides:
                    list_.append(side_1)
                self.__sides = list_
            else:
                self.__sides = [1 for _ in range(self.sides_count)]
        self.__color = color
        self.filled = filled
    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        flag = 0
        for color in (r, g, b):
            if color in range(0, 255):
                flag += 1
        if flag == 3:
            return True
        else:
            return False
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    def __is_valid_sides(self, *args):
        if self.sides_count == len(args):
            flag_ = 0
            for side_ in args:
                if isinstance(side_, int) and side_ > 0:
                    flag_ += 1
            if flag_ == self.sides_count:
                return True
        else:
            return False
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = []
            for el in new_sides:
                self.__sides.append(el)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides, filled=True):
        super().__init__(color, *sides, filled=True)
        self.__radius = len(self) / 2 * math.pi
    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        half_per = len(self) / 2
        num_ = 1
        for side_tri in self.get_sides():
            num_ *= (half_per - side_tri)
        return math.sqrt(half_per * num_)

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides, filled=True):
        super().__init__(color, *sides)

    def get_volume(self):
        return self._Figure__sides[0] ** 3

if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())