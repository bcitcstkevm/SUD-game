"""
Unit test for class Char
"""

# Kevin Mark
# A01067248
# Nov 21, 2018

from unittest import TestCase
from character import Char
from unittest.mock import patch
import io


class TestChar(TestCase):
    def setUp(self):
        self.testing_char = Char()

    def test_move_north(self):
        self.testing_char.set_y(5)
        self.testing_char.move_north()
        self.assertEqual(self.testing_char.get_y(), 4)

    def test_move_south(self):
        self.testing_char.set_y(5)
        self.testing_char.move_south()
        self.assertEqual(self.testing_char.get_y(), 6)

    def test_move_west(self):
        self.testing_char.set_x(5)
        self.testing_char.move_west()
        self.assertEqual(self.testing_char.get_x(), 4)

    def test_move_east(self):
        self.testing_char.set_x(5)
        self.testing_char.move_east()
        self.assertEqual(self.testing_char.get_x(), 6)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_increase_hp_check_io(self, mock_stdout):
        self.testing_char.set_hp(5)
        self.testing_char.increase_hp()
        self.assertEqual(mock_stdout.getvalue(), 'You have gained one hp\nYour hp is 6\n')

    def test_increase_hp_check_hp(self):
        self.testing_char.set_hp(5)
        self.testing_char.increase_hp()
        self.assertEqual(self.testing_char.get_hp(), 6)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_dead_check_io_alive(self, mock_stdout):
        self.testing_char.set_hp(1)
        self.testing_char.is_dead()
        self.assertEqual(mock_stdout.getvalue(), 'Your hp is 1.\nYou may want to keep walking.\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_dead_check_io_dead_zero(self, mock_stdout):
        self.testing_char.set_hp(0)
        self.testing_char.is_dead()
        self.assertEqual(mock_stdout.getvalue(), 'You are dead\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_dead_check_io_dead_negative(self, mock_stdout):
        self.testing_char.set_hp(-1)
        self.testing_char.is_dead()
        self.assertEqual(mock_stdout.getvalue(), 'You are dead\n')

    def test_is_dead_dead_zero(self):
        self.testing_char.set_hp(0)
        self.testing_char.is_dead()
        self.assertEqual(self.testing_char.get_dead(), True)

    def test_is_dead_dead_positive(self):
        self.testing_char.set_hp(5)
        self.testing_char.is_dead()
        self.assertEqual(self.testing_char.get_dead(), False)

    def test_is_dead_dead_negative(self):
        self.testing_char.set_hp(-1)
        self.testing_char.is_dead()
        self.assertEqual(self.testing_char.get_dead(), True)
