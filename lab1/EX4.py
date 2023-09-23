my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

# Используем функцию sorted() для сортировки словаря по значениям в убывающем порядке
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

# Получаем первые три элемента из отсортированного словаря
top_three = sorted_dict[:3]

# Извлекаем ключи из результатов
top_keys = [item[0] for item in top_three]

print("Три ключа с самыми высокими значениями:")
print(top_keys)
