"""
COMP 1510 Assignment - Game Class
"""

# Kevin Mark
# A01067248
# Nov 19, 2018


from fight import Fight
from monster import Genji
import utility
from character import Char
import json


class Game:
    def __init__(self, player: Char) -> None:
        """
        Initialize the Game

        PARAM: player, a Char object
        PRECONDITION: player is an object initialized from the Char class
        POSTCONDITION: Simulate a DND game
        RETURN: None
        """
        self.player = player
        self.min_x = 5
        self.max_x = 5
        self.min_y = 5
        self.max_y = 5
        self.scenario = {'0/0': "You dive into Lake Lum.",
                         '0/1': "You approach Lake Lum. As you stare out into the clearing, you take a deep breath",
                         '0/2': "You move up the River Lum. You feel as if you are being watched.",
                         '0/3': "You take a step towards the River Lum. You see a swarm of salmon swimming up the"
                                " river",
                         '0/4': "A group of goblins are sitting around a campfire. A goblin throws"
                                " his spear at you, but he misses.",
                         '1/0': "You swim up to the banks of Lake Lum",
                         '1/1': "You meet a kid dressed up in a monkey suit. You wonder what his doing.",
                         '1/2': "A Tracer blinks towards you. She waves and teleports to another dimension.",
                         '1/3': "You are standing at the gates of Lumbridge. You are looking towards the River Lum."
                                "\nDuke Horicio approaches you and says 'Walk out into the world but be"
                                " aware of the Genji'",
                         '1/4': "An old man approaches you. He seems to want some money.",
                         '2/0': "You walk into the woods.",
                         '2/1': "A giant snake slithers by.",
                         '2/2': "A yucky yellow bee buzzes by.",
                         '2/3': "A pruned Python Class counts its Cats",
                         '2/4': "The road you are walking on seems bumpy. You notice it is a very sunny day.",
                         '3/0': "You arrive at the Gates of Oasis. You pass through.",
                         '3/1': "You arrive at Matt's Inn. You have a drink",
                         '3/2': "You see a helpless Derrick. You leave him by the side of the road. Shame!",
                         '3/3': "You sit and enjoy some Pita.",
                         '3/4': "You are at the Gates of Varrock. Two guards stare at you menacingly.",
                         '4/0': "You are stopped by two guards. You do not have enough money to enter the"
                                " City of Oasis",
                         '4/1': "You arrive at the Gates of Oasis. You pass through",
                         '4/2': "You are in the woods south of Oasis. Seems eerily quiet. You remember the warning"
                                " about the Genji",
                         '4/3': "You are at the Gates of Varrock. Two guards stare at you menacingly.",
                         '4/4': "Welcome Adventurer to the City of Varrock"}

    def set_player_name(self) -> None:
        """
        Set player name

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        """
        # set player name
        user_input = input('Enter a name: ')
        self.player.set_name(user_input)
        # handle json code
        self.load_game()

    def load_game(self) -> None:
        """
        Load previous game

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        """
        file_name = 'saved_character.json'
        with open(file_name) as json_obj:
            data = json.load(json_obj)
            if data['name'] == self.player.get_name():
                # overwrite default attributes
                self.player.set_hp(data['hp'])
                self.player.set_x(data['x'])
                self.player.set_y(data['y'])
                print('Your previous character has been loaded')
            else:
                print('A new character has been created')

    # the code above is always executed at time of class initialization.

    def game_loop(self) -> None:
        """
        Game Loop

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        """
        user_input = ''
        while user_input != 'quit' and not self.player.get_dead():

            # prints instructions on how to control game
            self.print_instructions(user_input)

            # set user input
            user_input = get_user_input()

            # save game if user types quit
            if user_input == 'quit':
                self.save_game()

            # movement code/check input
            self.check_user_input(user_input)

            # next function controls what happens after a move is successfully made
            self.if_character_has_successfully_moved()

            # reset the move tracker to default value False
            self.player.set_has_character_not_moved(False)

    def print_instructions(self, user_input: str) -> None:
        """
        Print instructions to quit game

        A helper for game_loop
        PARAM: user_input, a string
        PRECONDITION: if user_input is not quit, the player is not dead, user input is not None
        POSTCONDITION: Prints instructions
        RETURN: None
        >>> test_char = Char()
        >>> test_game = Game(test_char)
        >>> test_game.print_instructions('not_correct_input')
        Try to walk some direction. Type "quit" anytime to exit and save
        """
        if user_input != 'quit' and not self.player.get_dead() and user_input:
            print('Try to walk some direction.', 'Type "quit" anytime to exit and save')

    def check_user_input(self, user_input: str) -> int:
        """
        Check user_input for correct directional input

        A helper for game_loop
        PARAM: user_input, a string
        PRECONDITION: user_input is a string
        POSTCONDITION: if user_input is 'north', 'south', 'east' or 'west', the game will proceed
        RETURN: int, int is used for unit testing.
        >>> test_char = Char()
        >>> test_game = Game(test_char)
        >>> test_game.check_user_input('north')
        A Tracer blinks towards you. She waves and teleports to another dimension.
          | 1 | 2 | 3 | 4 | 5
        ____________________
        1 |   |   |   |   |
        2 |   |   |   |   |
        3 |   | X |   |   |
        4 |   |   |   |   |
        5 |   |   |   |   |
        ____________________
        1
        """
        if user_enters_right_input_for_direction(user_input):
            self.move_character(user_input)
            return 1
        else:
            # if set_has_character_has_not_moved == true, Means the character did not make a legitimate move
            self.player.set_has_character_not_moved(True)
            print_wrong_input_message(user_input)
            return 2

    def move_character(self, user_input: str) -> None:
        """
        Move the character

        A helper for check_user_input.
        PARAM: user_input, a string
        PRECONDITION: user_input is from check_user_input, and character is not on any boundary
        POSTCONDITION: character will be moved accordingly, scenario and map will be printed
        RETURN: None
        >>> test_char = Char()
        >>> test_game = Game(test_char)
        >>> test_char.set_y(2)
        >>> test_game.move_character('north')
        You meet a kid dressed up in a monkey suit. You wonder what his doing.
          | 1 | 2 | 3 | 4 | 5
        ____________________
        1 |   |   |   |   |
        2 |   | X |   |   |
        3 |   |   |   |   |
        4 |   |   |   |   |
        5 |   |   |   |   |
        ____________________
        >>> test_char.get_y()
        1
        """

        if user_input == 'north' and self.not_on_northern_boundary():
            self.player.move_north()
        elif user_input == "west" and self.not_on_western_boundary():
            self.player.move_west()
        elif user_input == 'south' and self.not_on_southern_boundary():
            self.player.move_south()
        elif user_input == 'east' and self.not_on_eastern_boundary():
            self.player.move_east()
        else:
            self.player.set_has_character_not_moved(True)
            print("Error 198- A magical force prevents you from moving that direction")

        self.print_scenario()
        self.print_map()

    # helpers for move_character
    # boundary checkers
    def not_on_northern_boundary(self) -> bool:
        """
        Check that Char is not on north boundary

        A helper for move_character.
        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: bool
        >>> test_char = Char()
        >>> test_game = Game(test_char)
        >>> test_char.set_y(4)
        >>> test_game.not_on_northern_boundary()
        True
        >>> test_char.set_y(5)
        >>> test_game.not_on_northern_boundary()
        False
        """
        return 0 < self.player.get_y() < self.max_y

    def not_on_western_boundary(self) -> bool:
        """
        Check that Char is not on western boundary

        A helper for move_character.
        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: bool
        >>> test_char = Char()
        >>> test_game = Game(test_char)
        >>> test_char.set_x(4)
        >>> test_game.not_on_western_boundary()
        True
        >>> test_char.set_x(5)
        >>> test_game.not_on_western_boundary()
        False
        """
        return 0 < self.player.get_x() < self.max_x

    def not_on_southern_boundary(self) -> bool:
        """
        Check that Char is not on southern boundary

        A helper for move_character.
        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: bool
        >>> test_char = Char()
        >>> test_game = Game(test_char)
        >>> test_char.set_y(3)
        >>> test_game.not_on_southern_boundary()
        True
        >>> test_char.set_y(4)
        >>> test_game.not_on_southern_boundary()
        False
        """
        return 0 <= self.player.get_y() < self.max_y - 1

    def not_on_eastern_boundary(self) -> bool:
        """
        Check that Char is not on eastern boundary

        A helper for move_character.
        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: bool
        >>> test_char = Char()
        >>> test_game = Game(test_char)
        >>> test_char.set_x(3)
        >>> test_game.not_on_eastern_boundary()
        True
        >>> test_char.set_x(4)
        >>> test_game.not_on_eastern_boundary()
        False
        """
        return 0 <= self.player.get_x() < self.max_x - 1

    # scenarios
    def print_scenario(self) -> None:
        """
        Print the scenario

        A helper for move_character.
        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> test_char = Char()
        >>> test_game = Game(test_char)
        >>> test_char.set_y(3)
        >>> test_char.set_x(1)
        >>> test_game.print_scenario()
        You are standing at the gates of Lumbridge. You are looking towards the River Lum.
        Duke Horicio approaches you and says 'Walk out into the world but be aware of the Genji'
        """
        print(self.scenario[str(self.player.get_x()) + '/' + str(self.player.get_y())])

    # prints map
    def print_map(self) -> None:
        """
        Print the map

        A helper for move_character.
        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> test_char = Char()
        >>> test_game = Game(test_char)
        >>> test_char.set_x(1)
        >>> test_char.set_y(3)
        >>> test_game.print_map()
          | 1 | 2 | 3 | 4 | 5
        ____________________
        1 |   |   |   |   |
        2 |   |   |   |   |
        3 |   |   |   |   |
        4 |   | X |   |   |
        5 |   |   |   |   |
        ____________________
        """
        self.print_top_line_of_map()
        print('_' * 20)
        self.print_body_of_map()
        print('_' * 20)

    def print_top_line_of_map(self) -> None:
        """
        Print the top line of the map

        A helper for print_map
        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> test_char = Char()
        >>> test_game = Game(test_char)
        >>> test_game.print_top_line_of_map()
          | 1 | 2 | 3 | 4 | 5
        """
        for k in range(self.max_x):
            if k == 0:
                print(" ", end='')
            if k == self.max_x - 1:
                print(' | ' + str(k + 1))
            else:
                print(' | ' + str(k + 1), end='')

    def print_body_of_map(self) -> None:
        """
        Print the body of the map

        A helper for print_map
        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> test_char = Char()
        >>> test_game = Game(test_char)
        >>> test_game.print_body_of_map()
        1 |   |   |   |   |
        2 |   |   |   |   |
        3 |   |   |   |   |
        4 |   | X |   |   |
        5 |   |   |   |   |
        """
        for i in range(self.max_y):
            print(i + 1, end='')
            for j in range(self.max_x):
                if i == self.player.get_y() and j == self.player.get_x():
                    print(' | X', end='')
                elif j == self.max_x - 1 and not(j == self.player.get_x() and i == self.player.get_y()):
                    print(' |', end='')
                else:
                    print(' |  ', end='')
            print('')

    def if_character_has_successfully_moved(self) -> int:
        """
        Check if character made a successful move

        A helper for game_loop
        PARAM: n/a
        PRECONDITION: The character must not have its "has_character_not_moved" attribute triggered,
         else this code will not run
        POSTCONDITION: increase hp and begin the Genji encounter
        RETURN: int, this int is for unit testing purposes
        >>> import random
        >>> random.seed(1)
        >>> n_char = Char()
        >>> n_game = Game(n_char)
        >>> n_char.set_has_character_not_moved(False)
        >>> n_game.if_character_has_successfully_moved()
        Hmm. You feel itchy, as if you are being observed.
        1
        """
        if not self.player.get_has_character_not_moved():
            self.player.increase_hp()
            self.start_monster_encounter()
            return 1
        else:
            return 2

    def start_monster_encounter(self) -> int:
        """
        Check the chance of finding a Genji

        A helper for if_character_has_successfully_moved
        PARAM: n/a
        PRECONDITION: ten_percent_chance must be true for fight to proceed
        POSTCONDITION: choose to fight genji or not
        RETURN: int, the int is for testing purposes
        >>> import random
        >>> random.seed(1)
        >>> n_char = Char()
        >>> n_game = Game(n_char)
        >>> n_game.start_monster_encounter()
        Hmm. You feel itchy, as if you are being observed.
        2
        """
        if utility.ten_percent_chance():
            self.fight_genji()
            return 1
        else:
            print("Hmm. You feel itchy, as if you are being observed.")
            return 2

    def fight_genji(self) -> None:
        """Simulate a fight against Genji

        A helper for start_monster_encounter
        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: initialize a Genji and a new fight
        RETURN: None
        """

        print('You meet a Genji. He glares at you.')
        new_genji = Genji()
        new_fight = Fight(self.player, new_genji)
        new_fight.choose_to_fight_or_run()

    # save game
    def save_game(self) -> None:
        """
        Save the current player attributes

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        """
        file_name = 'saved_character.json'
        to_save = {"name": self.player.get_name(),
                   "hp": self.player.get_hp(),
                   "x": self.player.get_x(),
                   "y": self.player.get_y()
                   }
        with open(file_name, 'w') as save_obj:
            json.dump(to_save, save_obj)
            print('Your game has been successfully saved')

    def get_player(self) -> Char:
        """
        Get the instance Player

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: Char
        """
        return self.player


# Static Functions
def get_user_input() -> str:
    """ Get user input

    A helper for game_loop
    PARAM: n/a
    PRECONDITION: n/a
    POSTCONDITION: n/a
    RETURN: str
    """
    return input("Enter response here: ")


# helper for check_user_input
def print_wrong_input_message(user_input: str) -> None:
    """ Print instructions for incorrect input

    A helper for check_user_input
    PARAM: user_input, a string
    PRECONDITION: user_input must not be quit
    POSTCONDITION: Prints error message
    RETURN: None
    >>> print_wrong_input_message("anything")
    Error 200- Your typing wrong input
    """
    if user_input != 'quit':
        print("Error 200- Your typing wrong input")


def user_enters_right_input_for_direction(right_input: str) -> bool:
    """ Check user_input

    A helper for check_user_input
    PARAM: right_input, a string
    PRECONDITION: right_input must be a string
    POSTCONDITION: checks for correct string
    RETURN: bool
    >>> user_enters_right_input_for_direction('north')
    True
    """
    return right_input == 'north' or right_input == "south" or right_input == "east" or right_input == "west"
