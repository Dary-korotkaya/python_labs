import numpy as np

# Заданные значения
N = 12 # Задайте значение N
np.random.seed(42)  # Для воспроизводимости результатов

# Генерация данных
X = np.column_stack([np.ones(12), np.arange(N, N + 12), np.random.randint(60, 82, size=12)])
Y = np.random.uniform(13.5, 18.6, size=12)

# Решение задачи 1.2
#формула лин регрессии обр матрица np.linalg.inv
A = np.linalg.inv(X.T @ X) @ X.T @ Y

# Вывод вектора оценок A
print("Вектор оценок A:", A)

# Проверка вектора A по формуле Y = a0 + a1*x1 + a2*x2
Y_pred = X @ A

# Вывод результатов проверки
print("Проверка:")
print("Исходные значения Y:", Y)
print("Полученные значения Y:", Y_pred)
