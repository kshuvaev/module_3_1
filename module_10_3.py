# Домашнее задание по теме "Блокировки и обработка ошибок"

import threading
import random
from time import sleep

class Bank:
    global balance

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            sleep(0.001)
            dep = random.randint(50, 500)

            if self.balance+dep >=500 and self.lock.locked()==True:
                self.lock.release()
            else:
                self.balance += dep
                print(f'Пополнение:{dep} .Баланс:{self.balance}')

    def take(self):
        for i in range(100):
            dep = random.randint(50, 500)
            if dep>self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            else:
                self.balance -= dep
                print(f'Снятие:{dep} .Баланс:{self.balance}')


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')