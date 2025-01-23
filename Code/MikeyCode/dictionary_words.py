import random
import sys

number_of_words = int(sys.argv[1])

with open("/usr/share/dict/words", "r") as file:
    all_words = [line.strip() for line in file]

random_words = random.choices(all_words, k=number_of_words)

print(" ".join(random_words))
