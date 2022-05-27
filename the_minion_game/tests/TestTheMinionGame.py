from os import path
import unittest
from the_minion_game import main

class TestTheMinionGame(unittest.TestCase):
    
    def test_stuart_win_with_banana(self):
        self.assertEqual('Stuart 12', main.minion_game('BANANA'))

    def test_kevin_win_with_baananas(self):
        self.assertEqual('Kevin 19', main.minion_game('BAANANAS'))
    
    def test_kevin_win_with_ananas(self):
        self.assertEqual('Kevin 12', main.minion_game('ANANAS'))

    def test_extremly_long_vowel(self):
        self.assertEqual('Kevin 50005000', main.minion_game('A' * 10000))

    def test_extremly_random_word_from_file(self): # Character count => 1,000,000 :3
        __dir = path.dirname(__file__)

        with open(__dir + '/test_text.txt', 'r') as f:
            word = f.readlines()
            self.assertEqual('Kevin 400173457964', main.minion_game(word[0]))

        f.close()


if __name__ == '__main__':
    unittest.main()