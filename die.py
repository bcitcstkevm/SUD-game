"""
COMP 1510 Assignment - Die Class
"""

# Kevin Mark
# A01067248
# Nov 19, 2018

import random


class Die:
    def __init__(self, number_of_sides: int) -> None:
        """ Initialize a Die Object

        PARAM: number_of_sides, a positive integer
        PRECONDITION: number_of_sides is a positive integer >=1
        POSTCONDITION: n/a
        RETURN: None
        """
        self.face_value = None
        self.number_of_sides = number_of_sides
        self.roll_die()

    def roll_die(self) -> None:
        """ Set face_vale to random int between 1 and number_of_sides

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> test_die = Die(5)
        >>> 1 <= test_die.get_face_value() <= 5
        True
        """
        self.face_value = random.randint(1, self.number_of_sides)

    # setters/ getters
    def get_face_value(self) -> int:
        """ Get the face value

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: int
        """
        return self.face_value

    def get_number_of_sides(self) -> int:
        """ Get the number of sides

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: int
        """
        return self.number_of_sides
