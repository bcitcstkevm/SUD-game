"""
COMP 1510 Assignment - Character Class
"""

# Kevin Mark
# A01067248
# Nov 19, 2018

from entity import Entity


class Char(Entity):
    def __init__(self) -> None:
        """ Initialize a Character Object

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        """
        Entity.__init__(self, 10)
        self.name = 'will_be_set_by_a_game'
        self.x = 1
        self.y = 3
        self.has_character_not_moved = False

    def move_north(self) -> None:
        """ Decrease Char's y by 1

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> new_char = Char()
        >>> new_char.set_y(5)
        >>> new_char.move_north()
        >>> new_char.get_y()
        4
        """
        self.y -= 1

    def move_south(self) -> None:
        """ Increase Char's y by 1

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> new_char = Char()
        >>> new_char.set_y(5)
        >>> new_char.move_south()
        >>> new_char.get_y()
        6
        """
        self.y += 1

    def move_west(self) -> None:
        """ Decrease Char's x by 1

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: n/a
        >>> new_char = Char()
        >>> new_char.set_x(5)
        >>> new_char.move_west()
        >>> new_char.get_x()
        4
        """
        self.x -= 1

    def move_east(self) -> None:
        """ Increase Char's x by 1

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> new_char = Char()
        >>> new_char.set_x(5)
        >>> new_char.move_east()
        >>> new_char.get_x()
        6
        """
        self.x += 1

    def increase_hp(self) -> None:
        """ Increase Char's Hp by 1 with associated print statements

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> new_char = Char()
        >>> new_char.set_hp(5)
        >>> new_char.increase_hp()
        You have gained one hp
        Your hp is 6
        >>> new_char.get_hp()
        6
        """
        if self.hp_btw_zero_n_ten():
            self.add_one_to_hp()
            print('You have gained one hp')
            print('Your hp is ' + str(self.hp))

    # method for dealing with character dying, used in fight class
    def is_dead(self) -> None:
        """ Set dead to True if Char's Hp < 0

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: n/a
        >>> instance = Char()
        >>> instance.set_hp(-1)
        >>> instance.is_dead()
        You are dead
        >>> instance.get_dead()
        True
        >>> instance = Char()
        >>> instance.set_hp(5)
        >>> instance.is_dead()
        Your hp is 5.
        You may want to keep walking.
        >>> instance.get_dead()
        False
        """
        if self.hp_less_than_zero():
            print("You are dead")
            self.set_dead(True)
        else:
            print('Your hp is ' + str(self.hp) + '.')
            print('You may want to keep walking.')

    # setters/getters
    def get_x(self) -> int:
        """
        Return the x position of Char

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: int
        """
        return self.x

    def set_x(self, x: int) -> None:
        """
        Set the x position of Char

        PARAM: x, an int between 0, 4
        PRECONDITION: X must be set such that the character is not placed outside the map, between 0,4 inclusive
        POSTCONDITION: set the x position of the Char
        RETURN: None
        """
        self.x = x

    def get_y(self) -> int:
        """
        Return the x position of Char

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: int
        """
        return self.y

    def set_y(self, y: int) -> None:
        """
        Set the y position of Char

        PARAM: y, an int between 0,4 inclusive
        PRECONDITION: y must be set such that the character is not placed outside the map, between 0,4 inclusive
        POSTCONDITION: set the y position of Char
        RETURN: None
        """
        self.y = y

    def get_name(self) -> str:
        """
        Return the name of Char

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: str
        """
        return self.name

    def set_name(self, name) -> None:
        """
        Set the name of Char

        PARAM: name, string
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        """
        self.name = name

    def get_has_character_not_moved(self) -> bool:
        """
        Return the status of whether the Char made a successful move

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: bool
        """
        return self.has_character_not_moved

    def set_has_character_not_moved(self, moved) -> None:
        """
        Set the status of whether the Char made a successful move

        PARAM: moved, bool
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        """
        self.has_character_not_moved = moved
