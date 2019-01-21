"""
Unit test for class Die
"""

# Kevin Mark
# A01067248
# Nov 21, 2018
from unittest import TestCase
from die import Die


class TestDie(TestCase):
    def setUp(self):
        self.testing_die_one = Die(1)
        self.testing_die_five = Die(5)

    def test_roll_die_one(self):
        self.assertEqual(self.testing_die_one.get_number_of_sides(), 1)

    def test_roll_die_five(self):
        self.assertTrue(1 <= self.testing_die_one.get_number_of_sides() <= 5)
