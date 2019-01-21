"""
COMP 1510 Assignment - Fight Class
"""

# Kevin Mark
# A01067248
# Nov 19, 2018

from die import Die
import utility
from character import Char
from monster import Genji


class Fight:
    def __init__(self, character: Char, genji: Genji) -> None:
        """ Initialize a Fight Object

        PARAM: character, a Char Object
                    genji, a Genji Object
        PRECONDITION: game, character, and genji must be an instance from their respective classes
        POSTCONDITION: simulate the fight
        RETURN: None
        """
        self.character = character
        self.genji = genji
        self.do_not_exit_fight = True

    # First step of the fight
    def choose_to_fight_or_run(self) -> int:
        """ Choose to fight or run

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: int, the int is for unit testing purposes
        """
        fight_or_run = ''
        fight_or_run = fight_input(fight_or_run)

        if fight_or_run == 'run':
            self.run_chance()
            return 1
        elif fight_or_run == 'fight':
            self.execute_fight()
            return 2
        else:
            return 3

    def run_chance(self) -> None:
        """ Check if character takes damage

        Helper for choose_to_run_or_fight
        PARAM: n/a
        PRECONDITION: User chose to run
        POSTCONDITION: Simulate a 'run'
        RETURN: None
        >>> import random
        >>> random.seed(1)
        >>> new_char = Char()
        >>> new_genji = Genji()
        >>> new_fight = Fight(new_char, new_genji)
        >>> new_fight.run_chance()
        You got away without any consequences
        """
        if utility.ten_percent_chance():
            self.take_damage_from_running_away()
        else:
            print("You got away without any consequences")

    def take_damage_from_running_away(self) -> None:
        """ Damage the character

        Helper for run_chance
        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> import random
        >>> random.seed(1)
        >>> new_char = Char()
        >>> new_genji = Genji()
        >>> new_fight = Fight(new_char, new_genji)
        >>> new_fight.take_damage_from_running_away()
        You took 2 damage
        Your hp is 8.
        You may want to keep walking.
        """
        new_die = Die(4)
        damage = new_die.get_face_value()
        self.character.reduce_hp_by(damage)
        print('You took ' + str(damage) + ' damage')
        self.character.is_dead()

    def execute_fight(self) -> None:
        """ Execute the fight

        Helper for choose_to_run_or_fight
        PARAM: n/a
        PRECONDITION: User chose to fight
        POSTCONDITION: Simulate the combat round until death
        RETURN: None
        """
        print('You have chosen to fight. Time to face Genji')

        stop_condition = self.check_stop()

        # Fight loop
        i = 1
        while stop_condition:
            print('Round :' + str(i))

            self.combat_round()

            if not self.get_do_not_exit_fight():
                break

            i += 1

            self.press_button_to_continue_interactivity()

        self.keep_walking_message()

    def press_button_to_continue_interactivity(self) -> int:
        """ Get user to press Enter to continue

        Helper for execute_fight
        PARAM: n/a
        PRECONDITION: Neither character nor genji can be dead
        POSTCONDITION: User presses Enter to continue
        RETURN: int, the return value is for testing purposes
        >>> new_char = Char()
        >>> new_genji = Genji()
        >>> new_fight = Fight(new_char, new_genji)
        >>> new_char.set_dead(True)
        >>> new_fight.press_button_to_continue_interactivity()
        2
        """
        if not self.character.get_dead() and not self.genji.get_dead():
            input("Press any keyboard button to continue")
            return 1
        else:
            return 2

    def keep_walking_message(self):
        """ Tell user to keep walking after fight

        Helper for execute_fight
        PARAM: n/a
        PRECONDITION: Character must still be alive
        POSTCONDITION: Print a message to keep walking
        RETURN: None
        >>> new_char = Char()
        >>> new_genji = Genji()
        >>> new_fight = Fight(new_char, new_genji)
        >>> new_char.set_dead(False)
        >>> new_fight.keep_walking_message()
        You may want to keep walking
        """
        if not self.character.get_dead():
            print('You may want to keep walking')

    def combat_round(self) -> None:
        """ Execute a combat round

        Helper for execute_fight
        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> import random
        >>> random.seed(1)
        >>> new_char = Char()
        >>> new_genji = Genji()
        >>> new_fight = Fight(new_char, new_genji)
        >>> new_fight.combat_round()
        You swing your sword at Genji and he takes 2 damage
        The Genji's hp is 3
        Genji blades you and does 1 damage
        Your hp is 9.
        You may want to keep walking.
        """
        self.character_strike()
        self.genji_strike()

    def character_strike(self) -> None:
        """ Execute the character attacking

        Helper for combat round
        PARAM: n/a
        PRECONDITION: character must still be alive and 'do_not_exit_fight' must be True
        POSTCONDITION: Simulate a character strike, trigger loop end if Genji dies
        RETURN: None
        >>> import random
        >>> random.seed(1)
        >>> new_char = Char()
        >>> new_genji = Genji()
        >>> new_fight = Fight(new_char, new_genji)
        >>> new_fight.character_strike()
        You swing your sword at Genji and he takes 2 damage
        The Genji's hp is 3
        """
        if not self.character.get_dead() and self.do_not_exit_fight:
            new_roll_for_player = Die(6)
            player_damage = new_roll_for_player.get_face_value()
            print('You swing your sword at Genji and he takes ' + str(player_damage) + ' damage')

            self.genji.reduce_hp_by(player_damage)
            self.genji.is_dead()
            self.check_loop_status()

    def genji_strike(self):
        """ Execute the character attacking

        Helper for combat_round
        PARAM: n/a
        PRECONDITION: genji must still be alive and 'do_not_exit_fight' must be True
        POSTCONDITION: Simulate a genji strike, trigger loop end if Character dies
        RETURN: None
        >>> import random
        >>> random.seed(1)
        >>> new_char = Char()
        >>> new_genji = Genji()
        >>> new_fight = Fight(new_char, new_genji)
        >>> new_fight.genji_strike()
        Genji blades you and does 2 damage
        Your hp is 8.
        You may want to keep walking.
        """
        if not self.genji.get_dead() and self.do_not_exit_fight:
            new_roll_for_genji = Die(4)
            genji_damage = new_roll_for_genji.get_face_value()
            print("Genji blades you and does " + str(genji_damage) + ' damage')

            self.character.reduce_hp_by(genji_damage)
            self.character.is_dead()
            self.check_loop_status()

    def check_loop_status(self) -> None:
        """ Trigger loop end if an entity dies

        Helper for character_strike, genji_strike
        PARAM: n/a
        PRECONDITION: an entity is dead
        POSTCONDITION: terminate the fight loop in execute_fight
        RETURN: None
        >>> new_char = Char()
        >>> new_genji = Genji()
        >>> new_fight = Fight(new_char, new_genji)
        >>> new_char.set_dead(False)
        >>> new_genji.set_dead(True)
        >>> new_fight.check_loop_status()
        >>> new_fight.get_do_not_exit_fight()
        False
        """
        if self.genji.get_dead() or self.character.get_dead():
            self.set_do_not_exit_fight(False)

    def check_stop(self) -> bool:
        """ Stop the fight loop if an entity is dead or do_not_exit_fight is triggered.

        Helper for execute_fight
        PARAM: n/a
        PRECONDITION: An entity is dead or 'do_not_exit_fight' is triggered
        POSTCONDITION: Return False for stopping_condition
        RETURN: Bool
        >>> new_char = Char()
        >>> new_genji = Genji()
        >>> new_fight = Fight(new_char, new_genji)
        >>> new_char.set_dead(False)
        >>> new_genji.set_dead(False)
        >>> new_fight.set_do_not_exit_fight(False)
        >>> new_fight.check_stop()
        False
        """
        return not (self.character.get_dead() or self.genji.get_dead()) and self.do_not_exit_fight

    # setters/getters
    def set_do_not_exit_fight(self, condition: bool) -> None:
        """ Set the do_not_exit_fight state

        PARAM: condition, a bool
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        """
        self.do_not_exit_fight = condition

    def get_do_not_exit_fight(self) -> bool:
        """ Return the do_not_exit_fight state

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: bool
        """
        return self.do_not_exit_fight


def fight_input(fight_or_run: str) -> str:
    """ Get input for fight, deal with invalid input

    Helper for choose_to_fight_or_run
    PARAM: fight_or_run, a string
    PRECONDITION: fight_or_run must be either 'fight' or 'run'
    POSTCONDITION: Return the correct string
    RETURN: Str
    """
    while not (fight_or_run == 'fight' or fight_or_run == 'run'):
        fight_or_run = input("Do you want to stab Genji?. Type fight or run: ")
    return fight_or_run
