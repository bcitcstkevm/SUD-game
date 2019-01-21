"""
Unit Tests for Class Game
"""

# Kevin Mark
# A01067248
# Nov 22, 2018
from unittest import TestCase
from unittest.mock import patch
from game import Game
from character import Char
import io


class TestGame(TestCase):
    def setUp(self):
        self.test_char = Char()
        self.test_game = Game(self.test_char)

    @patch('builtins.input', return_value='jeff')
    def test_set_player_name(self, mock_name):
        self.test_game.set_player_name()
        self.assertEqual(self.test_char.get_name(), 'jeff')

    @patch('json.load', return_value={"name": "jeff", "hp": 7, "x": 4, "y": 0})
    def test_load_game(self, mock_json_obj):
        self.assertEqual(self.test_char.get_hp(), 10)
        self.assertEqual(self.test_char.get_x(), 1)
        self.assertEqual(self.test_char.get_y(), 3)
        self.test_char.set_name('jeff')
        self.test_game.load_game()
        self.assertEqual(self.test_char.get_hp(), 7)
        self.assertEqual(self.test_char.get_x(), 4)
        self.assertEqual(self.test_char.get_y(), 0)

    @patch('json.load', return_value={"name": "not_jeff", "hp": 7, "x": 4, "y": 0})
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_load_game_check_io_new_char(self, mock_output, json_output):
        self.test_char.set_name('jeff')
        self.test_game.load_game()
        self.assertEqual(mock_output.getvalue(), 'A new character has been created\n')

    @patch('json.load', return_value={"name": "jeff", "hp": 7, "x": 4, "y": 0})
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_load_game_check_io_(self, mock_output, json_output):
        self.test_char.set_name('jeff')
        self.test_game.load_game()
        self.assertEqual(mock_output.getvalue(), 'Your previous character has been loaded\n')

    @patch('game.get_user_input', return_value='quit')
    @patch('game.Game.save_game', return_value='test')
    @patch('game.Game.check_user_input', return_value='test')
    @patch('game.Game.if_character_has_successfully_moved', return_value='test')
    def test_game_loop_quit(self, mock_moved, mock_input, mock_save, mock_user):
        self.test_game.game_loop()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions(self, mock_output):
        self.test_char.set_dead(False)
        self.test_game.print_instructions('test_string')
        self.assertEqual(mock_output.getvalue(), 'Try to walk some direction. Type "quit" anytime to exit and save\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions_dead(self, mock_output):
        self.test_char.set_dead(True)
        self.test_game.print_instructions('test_string')
        self.assertEqual(mock_output.getvalue(), '')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions_quit(self, mock_output):
        self.test_char.set_dead(False)
        self.test_game.print_instructions('quit')
        self.assertEqual(mock_output.getvalue(), '')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructions_empty_str(self, mock_output):
        self.test_char.set_dead(True)
        self.test_game.print_instructions('')
        self.assertEqual(mock_output.getvalue(), '')

    @patch('game.Game.move_character', return_value='')
    @patch('game.print_wrong_input_message', return_value='')
    @patch('game.user_enters_right_input_for_direction', return_value=True)
    def test_check_user_input_true(self, mock_bool, mock_print, mock_move):
        self.assertEqual(self.test_game.check_user_input('north'), 1)

    @patch('game.Game.move_character', return_value='')
    @patch('game.print_wrong_input_message', return_value='')
    @patch('game.user_enters_right_input_for_direction', return_value=False)
    def test_check_user_input_true(self, mock_bool, mock_print, mock_move):
        self.assertEqual(self.test_game.check_user_input('north'), 2)

    def test_move_character_north(self):
        self.test_char.set_y(2)
        self.test_game.move_character('north')
        self.assertEqual(self.test_char.get_y(), 1)

    def test_move_character_south(self):
        self.test_char.set_y(2)
        self.test_game.move_character('south')
        self.assertEqual(self.test_char.get_y(), 3)

    def test_move_character_east(self):
        self.test_char.set_x(2)
        self.test_game.move_character('east')
        self.assertEqual(self.test_char.get_x(), 3)

    def test_move_character_west(self):
        self.test_char.set_x(2)
        self.test_game.move_character('west')
        self.assertEqual(self.test_char.get_x(), 1)

    def test_move_character_invalid(self):
        self.test_char.set_y(2)
        self.test_game.move_character('asfddasfa')
        self.assertEqual(self.test_char.get_has_character_not_moved(), True)

    @patch('game.Game.print_scenario', return_value='')
    @patch('game.Game.print_map', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_invalid_check_io(self, mock_obj, scenario, pri_map):
        self.test_char.set_y(2)
        self.test_game.move_character('asfddasfa')
        self.assertEqual(mock_obj.getvalue(), "Error 198- A magical force prevents you from moving that direction\n")

    def test_not_on_northern_boundary_inside(self):
        self.test_char.set_y(4)
        self.assertTrue(self.test_game.not_on_northern_boundary())

    def test_not_on_northern_boundary_outside_negative(self):
        self.test_char.set_y(0)
        self.assertTrue(not self.test_game.not_on_northern_boundary())

    def test_not_on_northern_boundary_outside_positive(self):
        self.test_char.set_y(5)
        self.assertTrue(not self.test_game.not_on_northern_boundary())

    def test_not_on_western_boundary_inside(self):
        self.test_char.set_x(4)
        self.assertTrue(self.test_game.not_on_western_boundary())

    def test_not_on_western_boundary_outside_negative(self):
        self.test_char.set_x(0)
        self.assertTrue(not self.test_game.not_on_western_boundary())

    def test_not_on_western_boundary_outside_positive(self):
        self.test_char.set_x(5)
        self.assertTrue(not self.test_game.not_on_western_boundary())

    def test_not_on_southern_boundary_inside(self):
        self.test_char.set_y(3)
        self.assertTrue(self.test_game.not_on_southern_boundary())

    def test_not_on_southern_boundary_outside_negative(self):
        self.test_char.set_y(-1)
        self.assertTrue(not self.test_game.not_on_southern_boundary())

    def test_not_on_southern_boundary_outside_positive(self):
        self.test_char.set_y(4)
        self.assertTrue(not self.test_game.not_on_southern_boundary())

    def test_not_on_eastern_boundary_inside(self):
        self.test_char.set_x(3)
        self.assertTrue(self.test_game.not_on_eastern_boundary())

    def test_not_on_eastern_boundary_outside_negative(self):
        self.test_char.set_x(-1)
        self.assertTrue(not self.test_game.not_on_eastern_boundary())

    def test_not_on_eastern_boundary_outside_positive(self):
        self.test_char.set_x(4)
        self.assertTrue(not self.test_game.not_on_eastern_boundary())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario(self, mock_output):
        self.test_char.set_x(1)
        self.test_char.set_y(3)
        self.test_game.print_scenario()
        self.assertEqual(mock_output.getvalue(), "You are standing at the gates of Lumbridge. You are looking"
                                                 " towards the River Lum.\nDuke Horicio approaches you and says"
                                                 " 'Walk out into the world but be aware of the Genji'\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map(self, mock_output):
        self.test_char.set_x(1)
        self.test_char.set_y(3)
        self.test_game.print_map()
        self.assertEqual(mock_output.getvalue(), """  | 1 | 2 | 3 | 4 | 5\n____________________\n1 |   |   |   |   \
|\n2 |   |   |   |   |\n3 |   |   |   |   |\n4 |   | X |   |   |\n5 |   |   |   |   |\n____________________\n""")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_top_line_of_map(self, mock_output):
        self.test_game.print_top_line_of_map()
        self.assertEqual(mock_output.getvalue(), '  | 1 | 2 | 3 | 4 | 5\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_body_of_map_top_left(self, mock_output):
        self.test_char.set_x(0)
        self.test_char.set_y(0)
        self.test_game.print_body_of_map()
        self.assertEqual(mock_output.getvalue(), """1 | X |   |   |   |\n2 |   |   |   |   |\n3 |   |   |   |   |\n4 \
|   |   |   |   |\n5 |   |   |   |   |\n""")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_body_of_map_top_right(self, mock_output):
        self.test_char.set_x(4)
        self.test_char.set_y(0)
        self.test_game.print_body_of_map()
        self.assertEqual(mock_output.getvalue(), """1 |   |   |   |   | X\n2 |   |   |   |   |\n3 |   |   |   |   |\n4 \
|   |   |   |   |\n5 |   |   |   |   |\n""")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_body_of_map_bottom_left(self, mock_output):
        self.test_char.set_x(0)
        self.test_char.set_y(4)
        self.test_game.print_body_of_map()
        self.assertEqual(mock_output.getvalue(), """1 |   |   |   |   |\n2 |   |   |   |   |\n3 |   |   |   |   |\n4 \
|   |   |   |   |\n5 | X |   |   |   |\n""")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_body_of_map_bottom_right(self, mock_output):
        self.test_char.set_x(4)
        self.test_char.set_y(4)
        self.test_game.print_body_of_map()
        self.assertEqual(mock_output.getvalue(), """1 |   |   |   |   |\n2 |   |   |   |   |\n3 |   |   |   |   |\n4 \
|   |   |   |   |\n5 |   |   |   |   | X\n""")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_body_of_map_top_boundary(self, mock_output):
        self.test_char.set_x(1)
        self.test_char.set_y(0)
        self.test_game.print_body_of_map()
        self.assertEqual(mock_output.getvalue(), """1 |   | X |   |   |\n2 |   |   |   |   |\n3 |   |   |   |   |\n4 \
|   |   |   |   |\n5 |   |   |   |   |\n""")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_body_of_map_left_boundary(self, mock_output):
        self.test_char.set_x(0)
        self.test_char.set_y(1)
        self.test_game.print_body_of_map()
        self.assertEqual(mock_output.getvalue(), """1 |   |   |   |   |\n2 | X |   |   |   |\n3 |   |   |   |   |\n4 \
|   |   |   |   |\n5 |   |   |   |   |\n""")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_body_of_map_right_boundary(self, mock_output):
        self.test_char.set_x(4)
        self.test_char.set_y(1)
        self.test_game.print_body_of_map()
        self.assertEqual(mock_output.getvalue(), """1 |   |   |   |   |\n2 |   |   |   |   | X\n3 |   |   |   |   |\n4 \
|   |   |   |   |\n5 |   |   |   |   |\n""")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_body_of_map_bottom_boundary(self, mock_output):
        self.test_char.set_x(1)
        self.test_char.set_y(4)
        self.test_game.print_body_of_map()
        self.assertEqual(mock_output.getvalue(), """1 |   |   |   |   |\n2 |   |   |   |   |\n3 |   |   |   |   |\n4 \
|   |   |   |   |\n5 |   | X |   |   |\n""")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_body_of_map_center(self, mock_output):
        self.test_char.set_x(2)
        self.test_char.set_y(2)
        self.test_game.print_body_of_map()
        self.assertEqual(mock_output.getvalue(), """1 |   |   |   |   |\n2 |   |   |   |   |\n3 |   |   | X |   |\n4 \
|   |   |   |   |\n5 |   |   |   |   |\n""")

    @patch('character.Char.increase_hp', return_value='')
    @patch('game.Game.start_monster_encounter', return_value='')
    def test_if_character_has_successfully_moved_not_moved(self, mock_game, mock_char):
        self.test_char.set_has_character_not_moved(True)
        self.assertEqual(self.test_game.if_character_has_successfully_moved(), 2)

    @patch('character.Char.increase_hp', return_value='')
    @patch('game.Game.start_monster_encounter', return_value='')
    def test_if_character_has_successfully_moved_not_moved(self, mock_game, mock_char):
        self.test_char.set_has_character_not_moved(False)
        self.assertEqual(self.test_game.if_character_has_successfully_moved(), 1)

    @patch('game.Game.fight_genji', return_value='')
    @patch('utility.ten_percent_chance', return_value=True)
    def test_start_monster_encounter(self, mock_chance, mock_fight):
        self.assertEqual(self.test_game.start_monster_encounter(), 1)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('utility.ten_percent_chance', return_value=False)
    def test_start_monster_encounter_no_chance(self, mock_chance, mock_input):
        self.assertEqual(self.test_game.start_monster_encounter(), 2)
        self.assertEqual(mock_input.getvalue(), 'Hmm. You feel itchy, as if you are being observed.\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('fight.Fight.choose_to_fight_or_run', return_value='')
    def test_fight_genji(self, mock_choice, mock_input):
        self.test_game.fight_genji()
        self.assertEqual(mock_input.getvalue(), 'You meet a Genji. He glares at you.\n')
