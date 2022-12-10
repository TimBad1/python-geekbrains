"""
При сравнении разных методов подсчёта факториала самым быстрым оказался метод
подключения математического модуля, затем, аж в 5 раз медленнее отработал цикл
и самый медленный результат у рекурсии и метода reduce при чём
с готовым массивом [1,2,3,4,5,6,7,8,9,10] работает в 2 раза дольше чем [i for i in range(1, 11)]
"""

from functools import reduce
import math
from memory_profiler import profile

@profile
def factorial_rec(n):
    """
    Подсчёт факториала через рекурсию
    """
    if n == 1:
        return 1
    return n * factorial_rec(n - 1)

# print(factorial_rec(5))

@profile
def factorial_cycle(n):
    """
    Подсчёт факториала циклом
    """
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p

# print(factorial_cycle(5))

@profile
def factorial_math(n):
    """
    Подсчёт факториала математическим модулем
    """
    return math.factorial(n)

@profile
def factorial_lc(n):
    """
    Подсчёт факториала методом reduce
    """
    return reduce(lambda x, y: x * y, [i for i in range(1, n + 1)])


factorial_rec(10)
factorial_cycle(10)
factorial_math(10)
factorial_lc(10)
