import math

# Ввод количества элементов и запись этих элементов в список
while True:
    try:
        n = int(input("Введите количество элементов: "))
        break  # Если ввод корректен, выходим из цикла
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целое число.")

el = []
i = 0

while i < n:
    try:
        num = int(input("Введите элемент: "))
        num_cubed = num ** 3
        el.append(num_cubed)
        i += 1
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целое число.")

print("Список элементов в кубе:", el)
print("Сумма элементов в списке:", sum(el))
print("Произведение элементов в списке:", math.prod(el))
