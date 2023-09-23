# Словарь с информацией о товарах
jewelry_store = {
    "Кольцо": ["Золото", 500, 10],
    "Серьги": ["Серебро", 300, 20],
    "Браслет": ["Серебро", 250, 15],
    "Ожерелье": ["Золото", 800, 5],
    "Часы": ["Серебро", 700, 8],
}

# Функция для просмотра описания
def view_description():
    for item, details in jewelry_store.items():
        print(f"{item} - {details[0]}")

# Функция для просмотра цены
def view_price():
    for item, details in jewelry_store.items():
        print(f"{item} - {details[1]} руб.")

# Функция для просмотра количества
def view_quantity():
    for item, details in jewelry_store.items():
        print(f"{item} - {details[2]} шт.")

# Функция для вывода всей информации
def view_all():
    for item, details in jewelry_store.items():
        print(f"{item} - {details[0]}, Цена: {details[1]} руб., Количество: {details[2]} шт.")

# Функция для покупки
def make_purchase():
    total_cost = 0
    while True:
        item_name = input("Введите название товара (или 'n' для завершения покупок): ")
        if item_name.lower() == 'n':
            break
        if item_name in jewelry_store:
            try:
                quantity = int(input(f"Введите количество {item_name}: "))
                if quantity > 0 and quantity <= jewelry_store[item_name][2]:
                    total_cost += quantity * jewelry_store[item_name][1]
                    jewelry_store[item_name][2] -= quantity
                    print(f"Добавлено {quantity} шт. {item_name} в корзину.")
                else:
                    print("Недостаточно товара на складе.")
            except ValueError:
                print("Ошибка ввода количества. Введите целое положительное число.")
        else:
            print("Такого товара нет в магазине.")
    print(f"Итоговая сумма покупки: {total_cost} руб.")
    print("Остатки товара в магазине:")
    view_all()

# Главное меню
while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        view_description()
    elif choice == '2':
        view_price()
    elif choice == '3':
        view_quantity()
    elif choice == '4':
        view_all()
    elif choice == '5':
        make_purchase()
    elif choice == '6':
        print("До свидания!")
        break
    else:
        print("Выберите корректный пункт меню.")
