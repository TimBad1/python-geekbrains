"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""

def my_div(arg_1, arg_2):
    """
    нахожнение частного от деления
    """
    if arg_2 == 0:
        print("На ноль делить нельзя")
        r = (input("Хотите повторить ввод данных? введите да: "))
        # if r.lower() == 'да':
        #     return my_div(int(input("Введите делимое: ")), int(input("Введите делитель: ")))
        # return 0
        return my_div(int(input("Введите делимое: ")), int(input("Введите делитель: "))) if r.lower() == 'да' else None
    return arg_1 / arg_2

print(my_div(int(input("Введите делимое: ")), int(input("Введите делитель: "))))
