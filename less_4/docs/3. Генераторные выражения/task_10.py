"""Модуль random как генератор псевдослучайных чисел"""

# Генерация дробных случайных чисел
from random import random, uniform, randint
print(random())  # -> 0.6225411844044528
print(random() * 10)  # -> 4.11167366154709
print(random() * (10 - 4) + 4)  # -> 8.993407001506782
