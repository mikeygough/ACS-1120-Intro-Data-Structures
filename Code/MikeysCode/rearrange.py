import random
import sys


if __name__ == "__main__":
    values = sys.argv[1:]
    random.shuffle(values)
    print(" ".join(values))
