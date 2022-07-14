import unittest
from string_validators import main

class TestStringValidators(unittest.TestCase):

    def test_all_false(self):
        self.assertEqual([False, False, False, False, False], main.string_validators(''))
        self.assertEqual([False, False, False, False, False], main.string_validators('\n'))
        self.assertEqual([False, False, False, False, False], main.string_validators('|$€'))
    
    def test_string_with_only_numbers(self):
        expected = [True, False, True, False, False]

        self.assertEqual(expected, main.string_validators('12345'))
        self.assertEqual(expected, main.string_validators('1'))

    def test_string_with_only_alpha_characters(self):
        self.assertEqual([True, True, False, True, True], main.string_validators('aBbczA'))
        self.assertEqual([True, True, False, True, False], main.string_validators('!asdfasdf#'))
        self.assertEqual([True, True, False, False, True], main.string_validators('WASDASDF'))

    def test_string_with_only_uppercase_characters(self):
        self.assertEqual([True, True, False, False, True], main.string_validators('ABBA'))
        self.assertEqual([True, True, True, False, True], main.string_validators('AWASD1ASD#'))

    def test_string_with_only_lowercase_characters(self):
        self.assertEqual([True, True, False, True, False], main.string_validators('acdc'))
        self.assertEqual([True, True, True, True, False], main.string_validators('1asdflol3'))


if __name__ == '__main__':
    unittest.main()