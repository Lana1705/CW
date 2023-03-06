class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = []

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, used_words={self.used_words})"

    def get_name(self):
        """Получаем имя"""
        return self.name

    def count_words(self):
        """получение количества использованных слов (возвращает int);"""
        return len(self.used_words)

    def add_word(self, word):
        """добавление слова в использованные слова (ничего не возвращает)"""
        self.used_words.append(word)

    def has_word_used(self, word):
        """проверка использования данного слова до этого (возвращает bool)"""
        return word.strip().lower() in self.used_words