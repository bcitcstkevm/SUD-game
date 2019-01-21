"""
Unit tests for Genji class
"""

# Kevin Mark
# A01067248
# Nov 21, 2018
from unittest import TestCase
from monster import Genji
import io
from unittest.mock import patch


class TestGenji(TestCase):
    def setUp(self):
        self.testing_instance = Genji()

    def test_is_dead_status_of_cat_not_dead(self):
        self.testing_instance.set_hp(3)
        self.testing_instance.is_dead()
        self.assertTrue(not self.testing_instance.get_dead())

    def test_is_dead_status_of_cat_dead_negative(self):
        self.testing_instance.set_hp(-1)
        self.testing_instance.is_dead()
        self.assertTrue(self.testing_instance.get_dead())

    def test_is_dead_status_of_cat_dead_zero(self):
        self.testing_instance.set_hp(0)
        self.testing_instance.is_dead()
        self.assertTrue(self.testing_instance.get_dead())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_dead_status_of_cat_print_alive(self, mock_stdout):
        self.testing_instance.set_hp(5)
        self.testing_instance.is_dead()
        self.assertEqual(mock_stdout.getvalue(), "The Genji's hp is 5\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_dead_status_of_cat_print_dead(self, mock_stdout):
        self.testing_instance.set_hp(-1)
        self.testing_instance.is_dead()
        self.assertEqual(mock_stdout.getvalue(), "You have killed Genji\n")
