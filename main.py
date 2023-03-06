from player import Player
from utils import load_random_word

PATH = "https://www.jsonkeeper.com/b/WT4Z"

def main():

    print("Введите имя игрока")

    user_name = input().title().strip()

    player = Player(name=user_name)
    basic_word = load_random_word(PATH)

    print(
    f"Привет, {player.get_name()}!\n"
    f"Составьте {basic_word.count_subwords()} слов из слова {basic_word.get_word().upper()}\n"
    f"Слова должны быть не короче 3 букв\n"
    f"Чтобы закончить игру, угадайте все слова или напишите 'stop'\n"
    f"Поехали, ваше первое слово?\n"
    )

    while player.count_words() != basic_word.count_subwords():

        user_input = input().strip().lower()

        if user_input in ["стоп", "stop"]:
            break

        elif len(user_input) < 3:
            print("Короткое слово")

        elif not basic_word.has_subwords(user_input):
            print("Такого слова нет")

        elif player.has_word_used(user_input):
            print("Уже использовано")

        else:
            print("Верно")
            player.add_word(user_input)

    print(f"Всего угадано {player.count_words()}")

main()