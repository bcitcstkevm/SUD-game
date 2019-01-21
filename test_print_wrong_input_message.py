"""
Unit test for print_wrong_input_message
"""

# Kevin Mark
# A01067248
# Nov 22, 2018

from unittest import TestCase
from game import print_wrong_input_message
from unittest.mock import patch
import io


class TestPrint_wrong_input_message(TestCase):
    def test_print_wrong_input_message_quit(self):
        self.assertEqual(print_wrong_input_message("quit"), None)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_wrong_input_message_quit(self, mock_output):
        print_wrong_input_message("asfas")
        self.assertEqual(mock_output.getvalue(), 'Error 200- Your typing wrong input\n')
