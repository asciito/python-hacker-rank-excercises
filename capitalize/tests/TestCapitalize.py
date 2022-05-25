import unittest
from capitalize import main

class TestCapitalize(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual('', main.capitalize(""))
    
    def test_simple_name(self):
        self.assertEqual('Alexander', main.capitalize('alexander'))

    def test_my_name(self):
        self.assertEqual('Ayax Córdova', main.capitalize('ayax córdova'))

    def test_too_many_whitespaces(self):
        self.assertEqual('Hello   World  You Lol', main.capitalize('hello   world  you lol'))

if __name__ == '__main__':
    unittest.main()