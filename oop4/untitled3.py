class Machine:
    # Атрибут класса
    total_machines = 0

    def __init__(self, name, category, color):
        # Атрибуты экземпляра
        self.name = name
        self.category = category
        self.color = color
        # Увеличиваем счетчик машин при каждом создании экземпляра
        Machine.total_machines += 1

    # Метод экземпляра
    def display_info(self):
        print(f"{self.color} {self.name} ({self.category})")

    # Статический метод
    @staticmethod
    def start_engine():
        print("Vroom! Vroom!")

    # Метод класса
    @classmethod
    def get_total_machines(cls):
        return cls.total_machines


# Пример использования
car1 = Machine("Toyota", "Sedan", "Blue")
car2 = Machine("Honda", "Hatchback", "Red")
bike = Machine("Harley", "Motorcycle", "Black")

# Вызываем методы экземпляра
car1.display_info()
car2.display_info()
bike.display_info()

# Вызываем статический метод
Machine.start_engine()

# Вызываем метод класса
total_machines = Machine.get_total_machines()
print(f"Total machines created: {total_machines}")
