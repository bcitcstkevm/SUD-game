"""
COMP 1510 Assignment - Monster Class
"""

# Kevin Mark
# A01067248
# Nov 19, 2018

from entity import Entity


class Genji(Entity):
    def __init__(self) -> None:
        """ Initialize a Genji Object

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        """
        Entity.__init__(self, 5)

    def is_dead(self) -> None:
        """ Check if Genji is dead

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> instance = Genji()
        >>> instance.set_hp(-1)
        >>> instance.is_dead()
        You have killed Genji
        >>> instance2 = Genji()
        >>> instance2.set_hp(3)
        >>> instance2.is_dead()
        The Genji's hp is 3
        """
        if self.hp_less_than_zero():
            print("You have killed Genji")
            self.set_dead(True)
        else:
            print("The Genji's hp is " + str(self.hp))
