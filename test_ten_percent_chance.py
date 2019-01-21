"""
Fill here
"""

# Kevin Mark
# A01067248
#
from unittest import TestCase
from unittest.mock import patch
from utility import ten_percent_chance


class TestTen_percent_chance(TestCase):
    @patch('die.Die.get_face_value', return_value=1)
    def test_ten_percent_chance(self, mock_result):
        self.assertTrue(ten_percent_chance())

    @patch('die.Die.get_face_value', return_value=3)
    def test_ten_percent_chance_no_chance(self, mock_result):
        self.assertTrue(not ten_percent_chance())
