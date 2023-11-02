with open("Клиент банка.txt", "w") as file:
    while True:
        str_file = input("Введите строку для записи в файл (ФИО счет дата рождения): ")
        if str_file == "":
            break
        file.write(str_file + '\n')

# Чтение данных из файла
with open("Клиент банка.txt", "r") as file:
    lines = file.readlines()

# Поиск клиентов с нулевым балансом и вычисление общей суммы вложений
total_investments = 0
zero_balance_clients = []

for line in lines:
    surname, balance, _ = line.strip().split()
    balance = int(balance)
    total_investments += balance
    if balance == 0:
        zero_balance_clients.append(surname)

# Вывод результатов
print("Фамилии клиентов с нулевым балансом:")
print(", ".join(zero_balance_clients))

print(f"Общая сумма вложений всех клиентов банка: {total_investments}")
