"""
При сравнении разных методов подсчёта факториала самым быстрым оказался метод
подключения математического модуля, затем, аж в 5 раз медленнее отработал цикл
и самый медленный результат у рекурсии и метода reduce при чём
с готовым массивом [1,2,3,4,5,6,7,8,9,10] работает в 2 раза дольше чем [i for i in range(1, 11)]
"""

from timeit import timeit
from factorial import factorial_rec, factorial_cycle, factorial_math, factorial_lc

print(timeit("factorial_rec(100)", setup="from __main__ import factorial_rec", number=100000))
print(timeit("factorial_cycle(100)", setup="from __main__ import factorial_cycle", number=100000))
print(timeit("factorial_math(100)", setup="from __main__ import factorial_math", number=100000))
print(timeit("factorial_lc(100)", setup="from __main__ import factorial_lc", number=100000))

"""
4.791663457
2.4407517799999994
0.5167011119999998
4.701772784
"""
