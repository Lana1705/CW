class BasicWord:

    def __init__(self, word="", subwords=None):

        self.word = word

        if subwords is None:
            self.subwords= []
        else:
            self.subwords = subwords

    def __repr__(self):
        return f"BasicWord(word={self.word}, subwords={self.subwords})"

    def count_subwords(self):
        """Возвращает количество подслов"""
        return len(self.subwords)

    def has_subwords(self, word_to_check):
        """Проверяет введеное слово в списке допустимых слов"""
        return word_to_check.strip().lower() in self.subwords

    def get_word(self):
        """Возвращает исходное слово"""
        return self.word
