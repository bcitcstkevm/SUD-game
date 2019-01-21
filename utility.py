"""
COMP 1510 Assignment - Utility Functions
"""

# Kevin Mark
# A01067248
# Nov 19, 2018

from die import Die


def ten_percent_chance() -> bool:
    """ Determine if within a 10% chance

    PARAM: n/a
    PRECONDITION: n/a
    POSTCONDITION: n/a
    RETURN: bool
    """
    chance = Die(10)
    random_number = chance.get_face_value()
    return random_number == 1
