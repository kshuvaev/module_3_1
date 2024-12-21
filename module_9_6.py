#  Домашнее задание по теме "Генераторы"

from itertools import combinations

def all_variants(text):
    for j in range(len(text)+1):
        for i in combinations(text, j):
            yield ''.join(i)

a = all_variants("abc")
for i in a:
    print(i)

