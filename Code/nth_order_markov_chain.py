#!python

from __future__ import division, print_function
import random
import pprint


class NthOrderMarkovChain(dict):
    def __init__(self, word_list=None, order=1):
        """Initialize"""
        super(NthOrderMarkovChain, self).__init__()

        self.order = order
        self.first_node = None

        # safety check
        if not word_list or len(word_list) <= order:
            return

        for index in range(len(word_list) - order):
            # create current_node
            current_node = tuple(word_list[index : index + order])

            if not self.first_node:
                self.first_node = current_node

            # create next_node
            # near the end... wrap
            if index + order + 1 > len(word_list):
                remaining = order - (len(word_list) - (index + 1))
                next_words = word_list[index + 1 :] + word_list[:remaining]
                next_node = tuple(next_words)
            else:
                next_node = tuple(word_list[index + 1 : index + order + 1])

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
        # safety check
        if node not in self or not self[node]:
            return None

        node_tokens = sum(self[node].values())
        dart = random.randint(1, node_tokens)
        fence = 0
        for next_node, count in self[node].items():
            fence += count
            if dart <= fence:
                return next_node
        return None

    def random_walk(self, count=5, first_word_mode="random"):
        # safety check
        if not self:
            return ""

        output = []

        # choose starting node
        if first_word_mode == "first":
            current_node = self.first_node
        else:
            current_node = random.choice(list(self.keys()))

        # add words
        output.extend(current_node)

        words_added = len(current_node)

        while words_added < count:
            next_node = self.sample_edge(current_node)
            if not next_node:
                break

            output.append(next_node[-1])
            words_added += 1
            current_node = next_node

        return " ".join(output[:count]) + "."

    def to_s(self):
        print(str(self))


def main():
    word_list = "I went left, you went right, I went left, I went right".split()
    chain = NthOrderMarkovChain(word_list)
    pprint.pprint(chain)
    print(chain.random_walk(50))


if __name__ == "__main__":
    main()
