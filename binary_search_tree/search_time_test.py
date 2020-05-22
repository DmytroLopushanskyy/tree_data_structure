"""
Module for testing time complexity of different realisations of BST.
"""
import random
import time
from linkedbst import LinkedBST


class CalculateTime:
    """
    Main calculation class.
    """
    def __init__(self):
        """
        Class initialisation. Setting up variables.
        """
        self.words_lst = list(self.read_file("words.txt"))
        self.tree = LinkedBST()
        self.unsorted_tree = LinkedBST()
        self.timer = 0

        for elem in self.words_lst[:990]:
            self.tree.add(elem)

        shuffled = random.sample(self.words_lst, 990)
        for elem in shuffled:
            self.unsorted_tree.add(elem)

    def test_lst_search(self):
        """
        Search in list calculations.
        """
        sample = self.get_random()
        lst = self.words_lst[:990]
        self.start_timer()
        for word in sample:
            lst.__contains__(word)

        self.stop_timer("List search result:")

    def test_sorted_bst_search(self):
        """
        Search in list calculations.
        """
        sample = self.get_random()
        self.start_timer()
        for word in sample:
            self.tree.find(word)

        self.stop_timer("Sorted BST search result:")

    def test_unsorted_bst_search(self):
        """
        Search in list calculations.
        """
        sample = self.get_random()
        self.start_timer()
        for word in sample:
            self.unsorted_tree.find(word)

        self.stop_timer("Not sorted BST search result:")

    def test_balanced_bst_search(self):
        """
        Search in list calculations.
        """
        sample = self.get_random()
        self.tree = self.tree.rebalance()
        self.start_timer()
        for word in sample:
            self.tree.find(word)
        self.stop_timer("Balanced BST search result:")

    def run_tests(self):
        """
        Runs all tests.
        """
        self.test_lst_search()
        self.test_sorted_bst_search()
        self.test_unsorted_bst_search()
        self.test_balanced_bst_search()

    def get_random(self):
        """
        Get random 990 words from dictionary.
        :return: iter
        """
        return random.sample(self.words_lst, 10000)

    def start_timer(self):
        """
        Starts timer.
        """
        self.timer = time.time()

    def stop_timer(self, text):
        """
        Stops timer and prints results.
        """
        print(text, time.time() - self.timer)

    @staticmethod
    def read_file(path):
        """
        (str) -> (set)
        Return a set of all words in the dictionary.
        """
        words = list()
        with open(path, encoding='utf-8', errors='ignore') as file:
            for line in file:
                line = line.strip().split()
                if not line:
                    continue
                words.append(line[0])
        return words  # random.sample(words, 10000)


if __name__ == '__main__':
    calc = CalculateTime()
    calc.run_tests()
