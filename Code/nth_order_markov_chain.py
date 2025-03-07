#!python

from __future__ import division, print_function
import random
import pprint

# TODO
# Make this truly an nth order markov chain based on the order arg


class NthOrderMarkovChain(dict):
    def __init__(self, word_list=None, order=2):
        """Initialize"""
        super(NthOrderMarkovChain, self).__init__()

        self.first_node = None

        for index, word in enumerate(word_list):
            # out of range error
            if index + 1 == len(word_list):
                break

            # create current_node
            current_node = (word, word_list[index + 1])
            if not self.first_node:
                self.first_node = current_node

            # create next_node
            # if last node, circle around
            if index + order > (len(word_list) - 1):
                next_node = (word_list[0], word_list[1])
            else:
                next_node = (word_list[index + 1], word_list[index + 2])

            # add if new
            if current_node not in self:
                self.add_new_node(current_node)

            # always update count
            self.add_edge(current_node, next_node)

    def add_new_node(self, current_node):
        self[current_node] = {}

    def add_edge(self, current_node, next_node, count=1):
        self[current_node][next_node] = self[current_node].get(next_node, 0) + count

    def sample_edge(self, node):
        node_tokens = sum(self[node].values())
        dart = random.randint(1, node_tokens)
        fence = 0
        for next_node, count in self[node].items():
            fence += count
            if dart <= fence:
                return next_node

    def random_walk(self, count=5, first_word_mode="random"):
        output = []

        if first_word_mode == "first":
            current_node = self.first_node
            output.append(self.first_node[0])
        else:
            current_node = random.choice(list(self.keys()))

        for i in range(count - 1):
            next_node = self.sample_edge(current_node)
            output.append(next_node[0])
            current_node = next_node

        return " ".join(output) + "."

    def to_s(self):
        print(str(self))


def main():
    word_list = "I went left, you went right, I went left, I went right".split()
    chain = NthOrderMarkovChain(word_list)
    pprint.pprint(chain)
    print(chain.random_walk(50))


if __name__ == "__main__":
    main()
