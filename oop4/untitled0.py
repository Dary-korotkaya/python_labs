class MyString:
    #
    def __init__(self, text):
        self.text = str(text)

    def length(self):
        return len(self.text)

    #объединение строк
    def united_str(self, other):
        self.text += other.text

    def to_upper(self):
        self.text = self.text.upper()

    def to_lower(self):
        self.text = self.text.lower()

    def display(self):
        return self.text


def main():
    print("Простой редактор для работы со строками.")

    input_text = input("Введите начальную строку: ")
    my_str = MyString(input_text)

    print("Длина строки:", my_str.length())

    input_text2 = input("Введите строку для объединения: ")
    other_str = MyString(input_text2)
    my_str.united_str(other_str)

    print("Объединенная строка:", my_str.display())

    my_str.to_upper()
    print("Строка в верхнем регистре:", my_str.display())

    my_str.to_lower()
    print("Строка в нижнем регистре:", my_str.display())


if __name__ == "__main__":
    main()
