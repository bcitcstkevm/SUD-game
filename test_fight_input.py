"""
Unit test for fight_input
"""

# Kevin Mark
# A01067248
# Nov 22, 2018

from unittest import TestCase
from unittest.mock import patch
from fight import fight_input

class TestFight_input(TestCase):

    @patch('builtins.input', return_value='fight')
    def test_fight_input(self, mock_output):
        self.assertEqual(fight_input(''), 'fight')

    @patch('builtins.input', return_value='run')
    def test_fight_input_run(self, mock_output):
        self.assertEqual(fight_input(''), 'run')

