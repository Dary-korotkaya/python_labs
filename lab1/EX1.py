total_seconds = 0

while True:
    try:
        user_input = int(input("Введите количество секунд (0 для завершения): "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    if user_input == 0:
        break

    total_seconds += user_input
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Прошло времени: {days} дней, {hours} часов, {minutes} минут, {seconds} секунд")

print("Завершено.")
