# Домашнее задание по теме "Потоки на классах"

import threading
from time import sleep

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        i = 0
        while 100-i*self.power > 0:
            sleep(1)
            i += 1
            print(f'{self.name} сражается {i} день(дня)..., осталось {100-i*self.power} воинов.')
        print(f'{self.name} одержал победу спустя {i} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
print('Все битвы закончились!')