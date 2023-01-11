"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент
рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например,
my_list = [7, 5, 3, 3, 2].
"""

# str_arr = input("Введите значения через пробел: ").split()
# num_arr = []
# for item in str_arr:
#     num_arr.append(int(item))
# print((sorted(num_arr, reverse=True)))

# num_arr.append(int(input("Добавьте число: ")))
# print((sorted(num_arr, reverse=True)))

# num_arr.append(int(input("Добавьте число: ")))
# print((sorted(num_arr, reverse=True)))

# num_arr.append(int(input("Добавьте число: ")))
# print((sorted(num_arr, reverse=True)))

my_list = [7, 5, 3, 3, 2]
while True:
    n = input("Введите оценку от 1 до 10 или q для выхода: ")
    if n != 'q':
        my_list.append(int(n))
        my_list.sort(reverse=True)
        print(my_list)
    else:
        break

my_list = sorted([7, 5, 3, 3, 2, int(input("Введите новый элемент рейтинга: "))], reverse=True)

print(my_list)
