"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file = open('file_2.txt', "r", encoding='utf-8')
count = 0
line_length = []
for line in file:
    count += 1
    print(len(line.split()))
print(f"{count} строк")
file.close()
