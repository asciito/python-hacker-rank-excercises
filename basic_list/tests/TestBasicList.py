import unittest
from basic_list import main
from .Context import PrintContext

class testBasicList(unittest.TestCase):

    def test_two_commands(self):
        arr = []

        # Append
        main.exec_command('append', arr, 10)

        self.assertListEqual([10], arr)

        # Insert
        main.exec_command('insert', arr, 100, 0)

        self.assertListEqual([100, 10], arr)

    def test_insert_at_the_begining(self):
        arr = []

        # Insert
        main.exec_command('insert', arr, 100, 0)

        self.assertListEqual([100], arr)

    def test_check_output(self):
        arr = []

        # Append
        main.exec_command('append', arr, 500)
        main.exec_command('append', arr, 50)
        main.exec_command('append', arr, 5)

        output = ''

        with PrintContext() as p:
            main.exec_command('print', arr)
            output = p.getValue()

        self.assertEqual('[500, 50, 5]', output)

    def test_sorting(self):
        arr = [10, 100, 23, 1, 1]

        # Remove the first occurence
        main.exec_command('remove', arr, 1)

        # Pop
        main.exec_command('pop', arr)

        # Append
        main.exec_command('append', arr, 33)

        # Insert
        main.exec_command('insert', arr, 1, 0)

        ## Assert Equal
        self.assertListEqual([1, 10, 100, 23, 33], arr)

        # Sort
        main.exec_command('sort', arr)

        ## Assert Sort
        self.assertListEqual([1, 10, 23, 33, 100], arr)
        

    def test_sorted_array(self):
        arr = []
