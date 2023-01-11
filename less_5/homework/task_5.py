"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""

from functools import reduce


with open("file_5.txt", "w", encoding="utf-8") as file:
    file.writelines(input("Введите числа через пробел: "))

with open("file_5.txt", "r", encoding="utf-8") as file:
    summ = reduce(lambda x, y: int(x) + int(y), file.readline().split())

    print(summ)
