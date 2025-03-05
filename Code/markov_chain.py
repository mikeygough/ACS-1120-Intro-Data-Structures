#!python

from __future__ import division, print_function
import random


class MarkovChain(dict):
    """MarkovChain is a..."""

    def __init__(self, word_list=None):
        """Initialize"""
        super(MarkovChain, self).__init__()

        self.first_word = ""

        # process words
        if word_list is not None and len(word_list) > 0:
            self.first_word = word_list[0]

            # add words
            for word in word_list:
                self.add_new_word(word)

            # add edges
            for index, word in enumerate(word_list):
                if index < len(word_list) - 1:
                    next_word = word_list[index + 1]
                    self.add_edge(word, next_word)

    def add_new_word(self, word):
        """Add word..."""
        is_new_word = word not in self
        if is_new_word:
            self[word] = {}
        return is_new_word

    def add_edge(self, current_word, next_word, count=1):
        if current_word not in self:
            self.add_new_word(current_word)

        if next_word not in self:
            self.add_new_word(next_word)

        self[current_word][next_word] = self[current_word].get(next_word, 0) + count

    def sample_edge(self, word):
        if word not in self or not self[word]:
            if len(self) > 0:
                return random.choice(list(self.keys()))
            return None

        word_tokens = sum(self[word].values())
        dart = random.randint(1, word_tokens)
        fence = 0
        for next_word, count in self[word].items():
            fence += count
            if dart <= fence:
                return next_word

        # fallback
        return random.choice(list(self[word].keys()))

    def random_walk(self, count=20, first_word_mode="random"):
        if not self:
            return ""

        sentence = []

        if first_word_mode == "first":
            current_word = self.first_word
        elif first_word_mode == "random":
            current_word = random.choice(list(self.keys()))
        else:
            current_word = (
                self.first_word if self.first_word else random.choice(list(self.keys()))
            )

        sentence.append(current_word)

        for i in range(count - 1):
            next_word = self.sample_edge(current_word)
            if next_word is None:
                break
            sentence.append(next_word)
            current_word = next_word

        sentence = " ".join(sentence)
        sentence += "."
        return sentence

    def to_s(self):
        print(str(self))


def main():
    word_list = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!".split()
    chain = MarkovChain(word_list)
    print(chain)
    print(chain.random_walk(5))


if __name__ == "__main__":
    main()
