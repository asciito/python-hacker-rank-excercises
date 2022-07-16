import unittest
from .. import main

class TestDoorMath(unittest.TestCase):
    def test_the_most_simle_case(self):
        self.assertEqual('WELCOME', main.door_mat(1, 1))
        self.assertEqual('WELCOME', main.door_mat(1, 3))

    def test_simple_size(self):
        self.assertEqual((
"""
---.|.---
-WELCOME-
---.|.---
""".strip()
        ), main.door_mat(3, 9))
        self.assertEqual((
"""
------.|.------
---.|..|..|.---
----WELCOME----
---.|..|..|.---
------.|.------
""".strip()
        ), main.door_mat(5, 15))
        self.assertEqual((
"""
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
""".strip()
        ), main.door_mat(7, 21))

    def test_is_to_big(self):
        self.assertEqual(445 * 1335 + 444, len(main.door_mat(445, 1335).strip()))
        self.assertEqual(999 * 2997 + 998, len(main.door_mat(999, 2997).strip()))