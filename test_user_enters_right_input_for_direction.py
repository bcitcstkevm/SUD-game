"""
Unit test for test_user_enters_right_input_for_direction
"""

# Kevin Mark
# A01067248
# Nov 22, 2018

from unittest import TestCase
from game import user_enters_right_input_for_direction

class TestUser_enters_right_input_for_direction(TestCase):
    def test_user_enters_right_input_for_direction_north(self):
        self.assertEqual(user_enters_right_input_for_direction('north'), True)

    def test_user_enters_right_input_for_direction_south(self):
        self.assertEqual(user_enters_right_input_for_direction('south'), True)

    def test_user_enters_right_input_for_direction_east(self):
        self.assertEqual(user_enters_right_input_for_direction('east'), True)

    def test_user_enters_right_input_for_direction_west(self):
        self.assertEqual(user_enters_right_input_for_direction('west'), True)

    def test_user_enters_right_input_for_direction_invalid(self):
        self.assertEqual(user_enters_right_input_for_direction('invalid'), False)
