class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером {self.title}")


# Пример использования
pen_instance = Pen("синей")
pencil_instance = Pencil("черным")
handle_instance = Handle("красным")

pen_instance.draw()    # Выведет: "Запуск отрисовки ручкой синей"
pencil_instance.draw() # Выведет: "Запуск отрисовки карандашом черным"
handle_instance.draw() # Выведет: "Запуск отрисовки маркером красным"
  