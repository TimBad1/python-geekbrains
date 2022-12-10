"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(var_1, var_2, var_3):
    """
    возвращает сумму наибольших двух аргументов
    """
    if var_1 >= var_3 and var_2 >= var_3:
        return var_1 + var_2
    if var_1 >= var_2 and var_3 >= var_2:
        return var_1 + var_3
    return var_2 + var_3

print(my_func(
    int(input("введите первое число: ")),
    int(input("введите второе число: ")),
    int(input("введите третье число: "))
))
