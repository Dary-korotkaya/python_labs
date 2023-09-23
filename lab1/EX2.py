try:
    text = input("Введите строку текста: ")

    # Перевод каждого символа в его код Unicode и сохранение в списке
    unicode_codes = [ord(char) for char in text]

    # Вывод кодов Unicode
    print("Коды Unicode символов:")
    for code in unicode_codes:
        print(code, end=" ")

    # Разделение строки на слова
    words = text.split()

    # Нахождение самого длинного слова
    longest_word = max(words, key=len)

    print("\nСамое длинное слово в строке:", longest_word)
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите корректную строку текста.")
