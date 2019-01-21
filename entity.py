"""
COMP 1510 Assignment - Entity Class
"""

# Kevin Mark
# A01067248
# Nov 19, 2018


class Entity:
    def __init__(self, hp) -> None:
        """ Initialize an Entity Object

        PARAM: hp, a positive integer > 0
        PRECONDITION: Hp must have a health value greater than 1
        POSTCONDITION: Create an entity object with health points
        RETURN: None
        """
        self.hp = hp
        self.dead = False

    def reduce_hp_by(self, damage: int) -> None:
        """ Reduce entity healthy by 'damage' amount

        Note reducing the entities hp below 0 is possible and will kill the entity
        PARAM: damage, a integer
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> instance = Entity(10)
        >>> instance.reduce_hp_by(5)
        >>> instance.get_hp()
        5
        """
        self.hp -= damage

    def hp_less_than_zero(self) -> bool:
        """ Return true if HP <= 0

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: bool
        >>> instance = Entity(10)
        >>> instance.set_hp(0)
        >>> instance.hp_less_than_zero()
        True
        >>> instance = Entity(10)
        >>> instance.set_hp(-1)
        >>> instance.hp_less_than_zero()
        True
        >>> instance = Entity(10)
        >>> instance.set_hp(5)
        >>> instance.hp_less_than_zero()
        False
        """
        return self.hp <= 0

    def hp_more_than_zero(self) -> bool:
        """ Return true if HP > 0

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: bool
        >>> instance = Entity(10)
        >>> instance.set_hp(0)
        >>> instance.hp_more_than_zero()
        False
        >>> instance = Entity(10)
        >>> instance.set_hp(-1)
        >>> instance.hp_more_than_zero()
        False
        >>> instance = Entity(10)
        >>> instance.set_hp(5)
        >>> instance.hp_more_than_zero()
        True
        """
        return self.hp > 0

    def add_one_to_hp(self) -> None:
        """ Add one to Hp

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: None
        >>> instance = Entity(10)
        >>> instance.set_hp(5)
        >>> instance.add_one_to_hp()
        >>> instance.get_hp()
        6
        """
        self.hp += 1

    def hp_btw_zero_n_ten(self) -> bool:
        """ Return true is hp is between 0 and 10, not inclusive

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: bool
        >>> instance = Entity(10)
        >>> instance.hp_btw_zero_n_ten()
        False
        >>> instance = Entity(10)
        >>> instance.set_hp(0)
        >>> instance.hp_btw_zero_n_ten()
        False
        >>> instance = Entity(10)
        >>> instance.set_hp(5)
        >>> instance.hp_btw_zero_n_ten()
        True
        """
        return 0 < self.hp < 10

    # setters/getters
    def get_hp(self) -> int:
        """
        Return the instance hp

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: int
        """
        return self.hp

    def set_hp(self, hp: int) -> None:
        """
        Set the instance hp

        PARAM: hp, an int
        PRECONDITION: You cannot set the instance to zero or less than zero
        POSTCONDITION: Set the instance hp
        RETURN: None
        """
        self.hp = hp

    def set_dead(self, dead: bool) -> None:
        """
        Set the instance dead status

        PARAM: dead, a bool
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: n/a
        """
        self.dead = dead

    def get_dead(self) -> bool:
        """
        Return the instance dead variable

        PARAM: n/a
        PRECONDITION: n/a
        POSTCONDITION: n/a
        RETURN: bool
        """
        return self.dead
