class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(f"Алфавит ({self.lang}): {', '.join(self.letters)}")

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self, lang='En'):
        super().__init__(lang, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "This is an example text in English."


# Пример использования
alphabet = Alphabet("Ru", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
alphabet.print()
print("Количество букв:", alphabet.letters_num())

eng_alphabet = EngAlphabet()
eng_alphabet.print()
print("Количество букв в английском алфавите:", eng_alphabet.letters_num())
print("Буква 'А' принадлежит английскому алфавиту?", eng_alphabet.is_en_letter('А'))
print("Пример текста на английском:", EngAlphabet.example())
