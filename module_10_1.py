# Домашнее задание по теме "Создание потоков"

import threading
import time
from time import sleep

def wite_words(word_count, file_name):
    with open(file_name, 'w') as file_:
        for i in range(word_count):
            file_.write(f'Какое-то слово № {i}')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_t = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
print(f'Работа потоков {time.time()-start_t}')

start_t = time.time()
thread1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
thread1.start()
thread2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
thread2.start()
thread3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
thread3.start()
thread4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))
thread4.start()

thread3.join()
print(f'Работа потоков {time.time()-start_t}')