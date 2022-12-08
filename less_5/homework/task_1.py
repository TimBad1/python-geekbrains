"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
file = open('my_file.txt', "r+", encoding='utf-8')
content = []
while True:
    line = f'{input("Введите строку: ")}\n'
    if line == '\n':
        break
    content.append(line)
    print(content)
file.writelines(content)

for line in file:
    print(line)

file.close()
