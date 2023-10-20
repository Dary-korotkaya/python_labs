def anagramm(str1, str2):
    # из строк в лист
    list1 = list(str1)
    list2 = list(str2)
    # сортировка значений листа
    list1.sort()
    list2.sort()

    i = 0
    matches = True

    while i < len(str1) and matches:
        if list1[i] == list2[i]:
            i = i + 1
        else:
            matches = False

    return matches


while True:
    s1 = input("Введите 1 слово для проверки (для выхода введите '0'): ")

    # Проверка на выход
    if s1 == '0':
        break

    s2 = input("Введите 2 слово для проверки : ")

    # Проверка на ввод строк
    if not isinstance(s1, str) or not isinstance(s2, str):
        print("Пожалуйста, введите корректные строки.")
        continue

    print(anagramm(s1, s2))
