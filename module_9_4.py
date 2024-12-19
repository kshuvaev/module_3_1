#   Домашнее задание по теме "Создание функций на лету"

from random import choice

class MysticBall:

    def __init__(self, *args):
        self.args = args

    def __call__(self):
        first_ball = choice(self.args)
        return  first_ball

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'a',encoding='utf-8')
        file.write(str(data_set))
        file.close()

    return write_everything


first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x,y: x==y, first, second)))

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())