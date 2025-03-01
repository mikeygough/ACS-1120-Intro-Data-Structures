#!python

from __future__ import division, print_function
import random


class MarkovChain(dict):
    """MarkovChain is a..."""

    def __init__(self, word_list=None):
        """Initialize"""
        super(MarkovChain, self).__init__()
        
        {one: {fish: 1},
         fish: {two: 1,
                red: 1,
                blue: 1},
         blue: {fish: 1}}

        self.first_word = ""
        # add new words
        if word_list is not None:
            self.first_word = word_list[0]
            for word in word_list:
                self.add_new_word(word)

        for index, word in enumerate(word_list):
            if index != 0:
                prev_word = word_list[index - 1]
                self.add_edge(prev_word, word)

    def add_new_word(self, word):
        """Add word..."""
        is_new_word = word not in self
        if is_new_word:
            self[word] = {}

    def add_edge(self, prev_word, word, count=1):
        self[prev_word][word] = self[prev_word].get(word, 0) + count

    def sample_edge(self, word):
        word_tokens = sum(self[word].values())
        # fix this to take into account last word
        dart = random.randint(1, word_tokens)
        fence = 0
        for key, value in self[word].items():
            fence += value
            if dart <= fence:
                return key

    def random_walk(self, count=10):
        sentence = []
        for i in range(count):
            if len(sentence) == 0:
                sentence.append(self.first_word)
            else:
                sentence.append(self.sample_edge(sentence[-1]))
        return " ".join(sentence)

    def to_s(self):
        print(self)


def main():
    word_list = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!".split()
    chain = MarkovChain(word_list)
    print(chain)
    print(chain.random_walk(5))


if __name__ == "__main__":
    main()
