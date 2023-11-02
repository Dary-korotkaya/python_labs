import os

'''
1. Создать программный файл F1 в текстовом формате, записать в него
построчно данные, вводимые пользователем. Об окончании ввода данных
будет свидетельствовать пустая строка. Скопировать в файл F2 только строки
из F1, которые не содержат цифр. Посчитать количество слов в последней
строке файла F2. 
'''

with open("F1.txt", "w") as f1:

    while True:
        str_file = input("Введите строку для записи в файл F1 (пустая строка для завершения): ")
        # Запись в файл
        f1.write(str_file + '\n')
        if str_file == "":
            break

with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    lines = f1.readlines()
    # Построчное извлечение из F1
    for line in lines:
        if not any(char.isdigit() for char in line):
            f2.write(line)

if lines:
    last_line = lines[-1].split()
    word_count = len(last_line)
    print(f"Количество слов в последней строке файла F2: {word_count}")
else:
    print("Файл F2 пуст.")