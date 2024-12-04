# Доп.задание по модулю:"Наследование классов."

import math

class Figure:
    sides_count = 0

    def __init__(self, __color, *args):
        self.__color = list(__color)
        self.__sides = list(args)
        self.filled = False

    def __str__(self):
        return f'{str(self.__sides[0])}'

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def __len__(self):
        per = 0
        for st in self.__sides:
            per += st
        return per

    def set_color(self, *args):
        self.args = args
        self.__is_valid_color()
        if self.filled == True:
            self.__color = list(args)
            return self.__color

    def __is_valid_color(self):

        for color_num in self.args:
            if isinstance(color_num, int):
                if color_num >= 0 and color_num <=256:
                    self.filled = True
                else:
                    self.filled = False
                    break
        return self.filled

    def set_sides(self, *new_sides):
        self.new_sides = new_sides
        self.__is_valid_sides()

        if self.count_side == True:
            self.__sides = list(new_sides)
            return self.__sides

    def __is_valid_sides(self):
        self.count_side = False

        if len(self.new_sides) == len(self.__sides):
            self.count_side = True
        else:
            t = 1
            if self.sides_count == 12 and (len(self.__sides) == 1):
                t = self.__sides[0]
            if self.sides_count == 12 and (len(self.new_sides) == 1):
                t = self.new_sides[0]
            self.__sides = list()
            for i in range(0, self.sides_count):
                self.__sides.append(t)
        return self.count_side


class Circle(Figure):
    sides_count = 1

    def get_square(self):  # площадь круга
        __radius = super().get_sides()
        if len(__radius) == self.sides_count:
            s_circle = int((__radius[0] / (2 * math.pi))**2*math.pi/2)
            return s_circle

class Triangle(Figure):
    sides_count = 3

    def get_square(self):  # площадь треугольника, формула Герона
        if len(super().get_sides()) == self.sides_count:
            s = 1 / 4 * math.sqrt(4 * super().get_sides()[0] ** 2 * super().get_sides()[1] ** 2
                                  - (super().get_sides()[0] ** 2 + super().get_sides()[1] ** 2
                                  - super().get_sides()[2] ** 2) ** 2)
            return s

class Cube(Figure):
    sides_count = 12

    def get_volume(self):  # объем куба
        if len(super().get_sides()) == self.sides_count:
            return super().get_sides()[0] ** 3

# (Цвет, стороны)
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
tri1 = Triangle((200, 200, 100), 10, 6, 5)

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

#tri1.set_sides(15, 20, 21)  # Изменится
#print(tri1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

#circle1.set_sides(10, 15, 6)  # круг - 1, то его стороны будут - [1]
#print(circle1.get_sides())
#tri1.set_sides(10, 6)  # треугольника - 3, то его стороны будут - [1, 1, 1]
#print(tri1.get_sides())
#cube1.set_sides(9)  # сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
#print(cube1.get_sides())
#cube1.set_sides(9, 12)  # сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
#print(cube1.get_sides())