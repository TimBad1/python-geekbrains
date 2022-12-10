"""
Реализация факториала разными методами
"""

from functools import reduce
import math


def factorial_rec(n):
    """
    Подсчёт факториала через рекурсию
    """
    if n == 1:
        return 1
    return n * factorial_rec(n - 1)

# print(factorial_rec(5))

def factorial_cycle(n):
    """
    Подсчёт факториала циклом
    """
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p

# print(factorial_cycle(5))

def factorial_math(n):
    """
    Подсчёт факториала математическим модулем
    """
    return math.factorial(n)

def factorial_lc(n):
    """
    Подсчёт факториала методом reduce
    """
    return reduce(lambda x, y: x * y, [i for i in range(1, n + 1)])
