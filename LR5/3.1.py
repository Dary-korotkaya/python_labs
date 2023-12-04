import numpy as np
import matplotlib.pyplot as plt

# Заданный интервал
t_values = np.arange(2, 3.05, 0.05)

# Формула функции
f_x = np.log(np.abs(1.3 + t_values)) - np.exp(t_values)

# Вывод значений аргумента и значения функции
for t, f in zip(t_values, f_x):
    print(f"t: {t:.2f}, f(t): {f:.4f}")

# Наибольшее, наименьшее, среднее значения и количество элементов массива
max_value = np.max(f_x)
min_value = np.min(f_x)
mean_value = np.mean(f_x)
num_elements = len(f_x)

# Сортировка массива (чётные варианты – по убыванию, нечётные – по возрастанию)
sorted_f_x = np.sort(f_x)[::-1] if num_elements % 2 == 0 else np.sort(f_x)

# Вывод статистики
print(f"\nНаибольшее значение: {max_value:.4f}")
print(f"Наименьшее значение: {min_value:.4f}")
print(f"Среднее значение: {mean_value:.4f}")
print(f"Количество элементов: {num_elements}")
print("\nОтсортированный массив:")
print(sorted_f_x)

# График изменения значений функции
plt.figure(figsize=(10, 6))
plt.plot(t_values, f_x, label='f(t)', marker='o')
plt.axhline(mean_value, color='r', linestyle='--', label='Mean Value')

# Оформление графика
plt.title('График изменения значений функции')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend()
plt.grid(True)
plt.show()
