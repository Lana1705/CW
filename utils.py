import random
from basic_word import BasicWord
import requests


def load_random_word(path):

    #получаем данные с сервера
    result = requests.get(path)
    status_code = result.status_code
    if status_code!=200:
        return None
    all_words_data = result.json()

    #получаем случайный словарь с данными
    random_word_data = random.choice(all_words_data)

    #создаем случайный экземпляр класса
    basic_word = BasicWord(
        word=random_word_data["word"],
        subwords=random_word_data["subwords"],
    )

    return basic_word