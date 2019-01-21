"""
Unit tests for class Fight
"""

# Kevin Mark
# A01067248
# Nov 22, 2018

from unittest import TestCase
from fight import Fight
from character import Char
from monster import Genji
from unittest.mock import patch
import io


class TestFight(TestCase):
    def setUp(self):
        self.play = Char()
        self.gen = Genji()
        self.fight = Fight(self.play, self.gen)

    @patch('fight.fight_input', return_value='')
    def test_choose_to_fight_or_run(self, mock_output):
        self.assertEqual(self.fight.choose_to_fight_or_run(), 3)

    @patch('fight.fight_input', return_value='fight')
    @patch('fight.Fight.execute_fight', return_value='fight executed')
    def test_choose_to_fight_or_run_fight(self, mock_execute_fight, mock_fight_input):
        self.assertEqual(self.fight.choose_to_fight_or_run(), 2)

    @patch('fight.fight_input', return_value='run')
    @patch('fight.Fight.run_chance', return_value='run_chance_executed')
    def test_choose_to_fight_or_run_run(self, mock_run, mock_input):
        self.assertEqual(self.fight.choose_to_fight_or_run(), 1)

    @patch('fight.Fight.take_damage_from_running_away', return_value='')
    @patch('utility.ten_percent_chance', return_value=True)
    def test_run_chance_true(self, mock_chance, mock_function):
        self.assertEqual(self.fight.run_chance(), None)

    @patch('utility.ten_percent_chance', return_value=False)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_chance_false(self, mock_output, mock_function):
        self.fight.run_chance()
        self.assertEqual(mock_output.getvalue(), "You got away without any consequences\n")

    @patch('die.Die.get_face_value', return_value=1)
    def test_take_damage_from_running_away(self, mock_die):
        self.play.set_hp(3)
        self.fight.take_damage_from_running_away()
        self.assertEqual(self.play.get_hp(), 2)

    @patch('die.Die.get_face_value', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_take_damage_from_running_away_check_io(self, mock_output, mock_die):
        self.play.set_hp(3)
        self.fight.take_damage_from_running_away()
        self.assertEqual(mock_output.getvalue(), 'You took 1 damage\nYour hp is 2.\nYou may want to keep walking.\n')

    @patch('builtins.input', return_value='test')
    @patch('die.Die.get_face_value', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_fight(self, mock_output, mock_die, mock_input):
        self.fight.execute_fight()
        self.assertEqual(mock_output.getvalue(), "You have chosen to fight. Time to face Genji\nRound :1\nYou swing"
                                                 " your sword at Genji and he takes 4 damage\nThe Genji's hp is "
                                                 "1\nGenji blades you and does 4 damage\nYour hp is 6.\nYou may want "
                                                 "to keep walking.\nRound :2\nYou swing your sword at Genji and "
                                                 "he takes 4 damage\nYou have killed Genji\nYou may want "
                                                 "to keep walking\n")

    def test_press_button_to_continue_interactivity_player_dead(self):
        self.play.set_dead(True)
        self.gen.set_dead(False)
        self.assertEqual(self.fight.press_button_to_continue_interactivity(), 2)

    def test_press_button_to_continue_interactivity_genji_dead(self):
        self.gen.set_dead(True)
        self.play.set_dead(False)
        self.assertEqual(self.fight.press_button_to_continue_interactivity(), 2)

    def test_press_button_to_continue_interactivity_both_dead(self):
        self.play.set_dead(True)
        self.gen.set_dead(True)
        self.assertEqual(self.fight.press_button_to_continue_interactivity(), 2)

    @patch('builtins.input', return_value='')
    def test_press_button_to_continue_interactivity_none_dead(self, mock_input):
        self.gen.set_dead(False)
        self.play.set_dead(False)
        self.assertEqual(self.fight.press_button_to_continue_interactivity(), 1)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_keep_walking_message(self, mock_output):
        self.play.set_dead(False)
        self.fight.keep_walking_message()
        self.assertEqual(mock_output.getvalue(), 'You may want to keep walking\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_keep_walking_message_true(self, mock_output):
        self.play.set_dead(True)
        self.fight.keep_walking_message()
        self.assertEqual(mock_output.getvalue(), '')

    @patch('die.Die.get_face_value', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round(self, mock_input, mock_chance):
        self.play.set_hp(10)
        self.gen.set_hp(5)
        self.fight.combat_round()
        self.assertEqual(mock_input.getvalue(), "You swing your sword at Genji and he takes 3 damage\nThe Genji's hp "
                                                "is 2\nGenji blades you and does 3 damage\nYour hp is 7.\nYou may want "
                                                "to keep walking.\n")

    @patch('die.Die.get_face_value', return_value=3)
    def test_character_strike_normal_conditions(self, mock_chance):
        self.play.set_dead(False)
        self.fight.set_do_not_exit_fight(True)
        self.gen.set_hp(5)
        self.fight.character_strike()
        self.assertEqual(self.gen.get_hp(), 2)

    @patch('die.Die.get_face_value', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_strike_check_io_normal(self, mock_input, mock_chance):
        self.play.set_dead(False)
        self.fight.set_do_not_exit_fight(True)
        self.gen.set_hp(5)
        self.fight.character_strike()
        self.assertEqual(mock_input.getvalue(), "You swing your sword at Genji and he takes 3 damage\nThe"
                                                " Genji's hp is 2\n")

    @patch('die.Die.get_face_value', return_value=3)
    def test_character_strike_char_dead(self, mock_chance):
        self.play.set_dead(True)
        self.fight.set_do_not_exit_fight(True)
        self.gen.set_hp(5)
        self.fight.character_strike()
        self.assertEqual(self.gen.get_hp(), 5)

    @patch('die.Die.get_face_value', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_strike_check_io_char_dead(self, mock_input, mock_chance):
        self.play.set_dead(True)
        self.fight.set_do_not_exit_fight(True)
        self.gen.set_hp(5)
        self.fight.character_strike()
        self.assertEqual(mock_input.getvalue(), '')

    @patch('die.Die.get_face_value', return_value=3)
    def test_character_strike_stop_trig(self, mock_chance):
        self.play.set_dead(False)
        self.fight.set_do_not_exit_fight(False)
        self.gen.set_hp(5)
        self.fight.character_strike()
        self.assertEqual(self.gen.get_hp(), 5)

    @patch('die.Die.get_face_value', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_strike_check_io_stop_trig(self, mock_input, mock_chance):
        self.play.set_dead(False)
        self.fight.set_do_not_exit_fight(False)
        self.gen.set_hp(5)
        self.fight.character_strike()
        self.assertEqual(mock_input.getvalue(), "")

    @patch('die.Die.get_face_value', return_value=3)
    def test_genji_strike_normal_conditions(self, mock_chance):
        self.gen.set_dead(False)
        self.fight.set_do_not_exit_fight(True)
        self.play.set_hp(5)
        self.fight.genji_strike()
        self.assertEqual(self.play.get_hp(), 2)

    @patch('die.Die.get_face_value', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_genji_strike_check_io_normal(self, mock_input, mock_chance):
        self.gen.set_dead(False)
        self.fight.set_do_not_exit_fight(True)
        self.play.set_hp(5)
        self.fight.genji_strike()
        self.assertEqual(mock_input.getvalue(), "Genji blades you and does 3 damage\nYour hp is 2.\nYou may"
                                                " want to keep walking.\n")

    @patch('die.Die.get_face_value', return_value=3)
    def test_genji_strike_gen_dead(self, mock_chance):
        self.gen.set_dead(True)
        self.fight.set_do_not_exit_fight(True)
        self.play.set_hp(5)
        self.fight.genji_strike()
        self.assertEqual(self.play.get_hp(), 5)

    @patch('die.Die.get_face_value', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_genji_strike_check_io_gen_dead(self, mock_input, mock_chance):
        self.gen.set_dead(True)
        self.fight.set_do_not_exit_fight(True)
        self.play.set_hp(5)
        self.fight.genji_strike()
        self.assertEqual(mock_input.getvalue(), '')

    @patch('die.Die.get_face_value', return_value=3)
    def test_genji_strike_stop_trig(self, mock_chance):
        self.gen.set_dead(False)
        self.fight.set_do_not_exit_fight(False)
        self.play.set_hp(5)
        self.fight.genji_strike()
        self.assertEqual(self.play.get_hp(), 5)

    @patch('die.Die.get_face_value', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_genji_strike_check_io_stop_trig(self, mock_input, mock_chance):
        self.gen.set_dead(False)
        self.fight.set_do_not_exit_fight(False)
        self.play.set_hp(5)
        self.fight.genji_strike()
        self.assertEqual(mock_input.getvalue(), "")

    def test_check_loop_status_if_both_dead(self):
        self.play.set_dead(True)
        self.gen.set_dead(True)
        self.fight.check_loop_status()
        self.assertEqual(self.fight.get_do_not_exit_fight(), False)

    def test_check_loop_status_if_char_dead(self):
        self.play.set_dead(True)
        self.gen.set_dead(False)
        self.fight.check_loop_status()
        self.assertEqual(self.fight.get_do_not_exit_fight(), False)

    def test_check_loop_status_if_gen_dead(self):
        self.play.set_dead(False)
        self.gen.set_dead(True)
        self.fight.check_loop_status()
        self.assertEqual(self.fight.get_do_not_exit_fight(), False)

    def test_check_loop_status_if_neither_dead(self):
        self.play.set_dead(False)
        self.gen.set_dead(False)
        self.fight.check_loop_status()
        self.assertEqual(self.fight.get_do_not_exit_fight(), True)

    def test_check_stop_char_dead(self):
        self.gen.set_dead(False)
        self.play.set_dead(True)
        self.fight.set_do_not_exit_fight(True)
        self.assertEqual(self.fight.check_stop(), False)

    def test_check_stop_genji_dead(self):
        self.gen.set_dead(True)
        self.play.set_dead(False)
        self.fight.set_do_not_exit_fight(True)
        self.assertEqual(self.fight.check_stop(), False)

    def test_check_stop_stop_triggered(self):
        self.gen.set_dead(False)
        self.play.set_dead(False)
        self.fight.set_do_not_exit_fight(False)
        self.assertEqual(self.fight.check_stop(), False)

    def test_check_stop_no_stop(self):
        self.gen.set_dead(False)
        self.play.set_dead(False)
        self.fight.set_do_not_exit_fight(True)
        self.assertEqual(self.fight.check_stop(), True)
