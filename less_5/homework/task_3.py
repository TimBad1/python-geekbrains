"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
from functools import reduce

file = open('file_3.txt', "r", encoding='utf-8')
content = file.readlines()
small_salary = tuple(el.split()[0] for el in content if float(el.split()[1]) < 20000)
average_salary = reduce(lambda x, y: x + y, [float(el.split()[1]) for el in content]) / len(content)
print(f'Средняя величина дохода сотрудников - {average_salary}')
print('У следующих сотрудников величина дохода < 20000:')
for el in small_salary:
    print(el)
file.close()
