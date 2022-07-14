import unittest
from .. import main
import textwrap

class TestTextWrap(unittest.TestCase):
    
    def test_no_string_input(self):
        self.assertEqual('', main.wrap('', 4))

    def test_exact_number_of_char_per_paragraph(self):
        string = 'fluffsteroffectinh'
        self.assertEqual(textwrap.fill(string, 3), main.wrap(string, 3))
        self.assertEqual(textwrap.fill(string, 6), main.wrap(string, 6))
        self.assertEqual(textwrap.fill(string, 3), main.wrap(string, 3))
    
    def test_last_part_is_not_the_exact_max_width(self):
        self.assertRegex(main.wrap('fluffsteroffectinh', 4), r'\nnh$')