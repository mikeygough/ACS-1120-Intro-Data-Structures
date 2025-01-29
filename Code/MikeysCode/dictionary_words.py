import random
import sys


def read_words():
    with open("/usr/share/dict/words", "r") as file:
        all_words = [line.strip() for line in file]
    return all_words


def get_random_words(all_words, number_of_words):
    random_words = random.choices(all_words, k=number_of_words)
    return random_words


if __name__ == "__main__":
    number_of_words = int(sys.argv[1])
    all_words = read_words()
    random_words = get_random_words(all_words, number_of_words)
    print(" ".join(random_words))
