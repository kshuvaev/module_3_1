import math

class Figure:
    sides_count = 0
    filled = False

    def __init__(self, __color,*args):
        self.__color = list(__color)
        self.__sides = list(args)

    def __str__(self):
        return f'{str(self.__sides[0])}'

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def set_color(self, r=int, g=int, b=int):
        if (r >= 0 and r <= 256) and (g >= 0 and g <= 256) and (b >= 0 and b <= 256):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b
            return self.__color

    def set_sides(self, *new_sides):

        if len(list(new_sides))==self.sides_count:
            self.__sides=list(new_sides)

        if len(list(new_sides)) ==1 and  self.sides_count==12:
            self.__sides = list()
            for i in range(0, self.sides_count):
                self.__sides.append(new_sides[0])

        if len(list(new_sides)) !=self.sides_count:
            if len(list(self.__sides)) == 1:
                t = self.__sides[0]
            else:
                t=1
            self.__sides = list()

            for i in range(0, self.sides_count):
                self.__sides.append(t)


class Circle(Figure):
    sides_count = 1

    def get_square(self):  # площадь круга
        super().get_sides()
        if len(super().get_sides())==self.sides_count:
            radius =super().get_sides()[0] / (2 * math.pi)
            return int(radius ** 2 * math.pi / 2)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):  # площадь треугольника
        if len(super().get_sides()) == self.sides_count:
            s=1/4*math.sqrt(4*super().get_sides()[0]**2*super().get_sides()[1]**2-
                            (super().get_sides()[0]**2+super().get_sides()[1]**2-super().get_sides()[2]**2)**2)
            return s

class Cube(Figure):
    sides_count = 12

    def get_volume(self): #объем куба
        if len(super().get_sides()) == self.sides_count:
            return super().get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
tri1=Triangle((200, 200, 100), 10, 6, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(circle1)

# Проверка объёма (куба):
print(cube1.get_volume())