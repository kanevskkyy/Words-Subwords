import os
from player import Player
from utils import load_random_word
from basic_word import BasicWord

def line():
    """print line"""
    print("=============================================")


def clear_console():
    """Function clear console"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def press_entry():
    """press enter to continue"""
    print("Нажміть Enter, щоб продовжити ...", end="")
    input()
    clear_console()


def print_statistic(player):
    """print statistic"""
    print(f"Гра завершена! Ви відгадали {player.amount_of_used_word()} слова ^_^")


DATA_SOURCE = "https://www.jsonkeeper.com/b/CQ22"
MIN_LETTERS = 3

user_name = input("Введіть ваший нікнейм = ")
line()

player = Player(user_name)
print(player)

random_word = load_random_word(DATA_SOURCE)
print(f"Складіть {random_word.amount_subwords()} слів зі слова {random_word.word}\nСлова не повинні бути коротші за {MIN_LETTERS} букви\nЩоб закінчити гру напишіть слово 'stop' або 'стоп'")
press_entry()

while random_word.amount_subwords() > 0:
    user_input = input("Поїхали ваше слово? Ввід = ")
    if user_input.lower() == "stop" or user_input.lower() == "стоп":
        clear_console()
        break

    if len(user_input) < MIN_LETTERS:
        print("Занадто коротке слово")
        press_entry()
        continue

    if random_word.check_enter_word(user_input) and player.check_word_not_used(user_input):
        print("Правильно!! Вітаємо)")
        player.add_word(user_input)
        random_word.subwords.remove(user_input)
        press_entry()
        continue
    
    if player.check_word_not_used(user_input) == False:
        print("Це слово вже було використане)")
        press_entry()
        continue

    if random_word.check_enter_word(user_input) == False:
        print("На жаль, це не те слово :(")
        press_entry()
        continue

print_statistic(player)