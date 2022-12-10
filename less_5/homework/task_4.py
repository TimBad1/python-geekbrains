"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open('file_4.txt', "r", encoding="utf-8") as read_file:
    with open('file_4_new.txt', "w", encoding="utf-8") as write_file:
        content = read_file.readlines()
        new_content = []

        for line in content:
            new_content.append(' '.join(
                [my_dict[item] if item in my_dict else item for item in line.split()]
                ) + '\n')
        print(new_content)
        write_file.writelines(new_content)