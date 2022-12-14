"""
Программа принимает действительное положительное число x и целое
отрицательное число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y). При решении
задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение встепень с помощью оператора *. Второй — более сложная
реализация без оператора *, предусматривающая использование цикла.
"""

def my_func(x, y):
    """
    возведение числа x в степень y
    """
    if y > -1:
        return None
    if y == -1:
        return 1 / x
    return (1 / x) * my_func(x, y + 1)

    res = 1
    while y < 0:
        res /= x
        y += 1
    return res

print(my_func(
    x=int(input("введите действительное положительное число: ")),
    y=int(input("введите целое отрицательное число: "))
    ))
