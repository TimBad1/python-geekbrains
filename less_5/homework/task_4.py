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


file = open('file_4.txt', "r", encoding='utf-8')
new_file = open('file_4_new.txt', "a", encoding='utf-8')
content = file.readlines()
# new_content = ''
for line in content:
    # new_content(str([my_dict[el] if el in my_dict else el for el in line]))

# new_content = [my_dict[el] if el in my_dict else el for el in line]


new_file.writelines(new_content)
file.close()
new_file.close()
