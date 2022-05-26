import sys
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


if __name__ == '__main__':
    unittest.main()