def fun(data):
    if isinstance(data, list):
        # Найти сумму всех элементов после последнего положительного
        pos = [i for i, num in enumerate(data) if num > 0]
        if pos:
            last_pos_ind = pos[-1]
            endsum = sum(data[last_pos_ind + 1:])
            # Удалить все нулевые элементы из списка
            data = [num for num in data if num != 0]
            return endsum, data
        else:
            return 0, data  # Если нет положительных чисел, сумма = 0, список без изменений
    elif isinstance(data, dict):
        # Вывести элемент с минимальным значением
        min_value = min(data.values())
        return min_value
    elif isinstance(data, int):
        # Вывести число в обратном порядке
        return int(str(data)[::-1])
    elif isinstance(data, str):
        # Определить количество слов в строке
        words = data.split()
        word_count = len(words)
        return word_count
    else:
        return "Тип данных не поддерживается"

# Примеры использования функции
print(fun([1, 2, 0, 3, 4, -1, 5]))             # Пример списка
print(fun({"a": 3, "b": 1, "c": 5}))           # Пример словаря
print(fun(12345))                              # Пример числа
print(fun("Пример строки для подсчета слов"))  # Пример строки
