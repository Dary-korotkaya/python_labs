def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
        result = None
    finally:
        print("Этот блок всегда выполняется, независимо от того, произошло исключение или нет.")
    return result

# Примеры вызова функции с разными аргументами
print("Пример 1:")
result1 = divide_numbers(10, 2)  # Нормальное деление
print("Результат:", result1)

print("Пример 2:")
result2 = divide_numbers(10, 0)  # Деление на ноль
print("Результат:", result2)

print("Пример 3:")
result3 = divide_numbers("10", 2)  # Некорректные аргументы (строка вместо числа)
print("Результат:", result3)
