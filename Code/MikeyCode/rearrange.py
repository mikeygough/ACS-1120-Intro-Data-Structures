import random
import sys

values = sys.argv[1:]
random.shuffle(values)
print(" ".join(values))
