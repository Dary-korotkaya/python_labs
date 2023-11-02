import json

# Чтение данных из файла и вычисление прибыли каждой компании
companies = []
total_profit = 0
profitable_companies_count = 0

with open("фирмы.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    name, form, revenue, costs = line.strip().split()
    revenue, costs = int(revenue), int(costs)
    profit = revenue - costs
    if profit > 0:
        total_profit += profit
        profitable_companies_count += 1
    companies.append({name: profit})

# Вычисление средней прибыли (если есть прибыльные компании)
average_profit = total_profit / profitable_companies_count if profitable_companies_count > 0 else 0

# Создание списка с JSON-объектами
result_list = [companies, {"average_profit": average_profit}]

# Сохранение списка в JSON-файл
with open("результат.json", "w", encoding="utf-8") as json_file:
    json.dump(result_list, json_file, ensure_ascii=False)

# Вывод JSON-объекта
print("JSON-объект успешно сохранен в файл 'результат.json'.")
with open("результат.json", "r", encoding="utf-8") as json_file:
    print(json_file.read())
