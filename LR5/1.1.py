import numpy as np

# Заданные значения
a = 0.3
b = -21.17

# Решение задачи 1.1
y = ((a + 1.5)**(1/3)) + ((a + b)**8) - (b / (np.arcsin(np.abs(a)**2)))

# Вывод результата
print("Результат выражения:", y)
