class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_owner(self,owner):
        self.owner=owner

    def get_model(self,__model):
        self.__model=__model
        return f'Модель: {__model}'

    def get_horsepower(self,__engine_power):
        self.__engine_power = __engine_power
        return f'Мощность двигателя: {__engine_power}'

    def get_color(self,__color):
        self.__color = __color
        return f'Цвет: {__color}'

    def print_info(self):
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец: {self.owner}')

    def set_color(self,new_color):
        if self.__COLOR_VARIANTS.count(new_color.lower())>0:
            self.__color=new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()