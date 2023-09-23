# Получаем ввод пользователя
user_input = input("Введите последовательность чисел, разделенных запятой: ")

try:
    # Разделяем строку на числа, используя запятую в качестве разделителя, и преобразуем их в целые числа
    numbers = [int(num.strip()) for num in user_input.split(',')]

    # Создаем список из введенных чисел
    numbers_list = numbers

    # Создаем кортеж из введенных чисел
    numbers_tuple = tuple(numbers)

    # Выводим результат
    print("Список чисел:", numbers_list)
    print("Кортеж чисел:", numbers_tuple)
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите числа, разделенные запятой.")