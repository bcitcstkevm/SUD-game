"""
FILE name
"""

# Kevin Mark
# A01067248
# Nov 21, 2018
from unittest import TestCase
from entity import Entity


class TestEntity(TestCase):

    def setUp(self):
        self.instance = Entity(10)

    def test_reduce_hp_by(self):
        self.instance.reduce_hp_by(5)
        self.assertEqual(5, self.instance.get_hp())

    def test_hp_less_than_zero_zero(self):
        self.instance.set_hp(0)
        self.assertTrue(self.instance.hp_less_than_zero())

    def test_hp_less_than_zero_negative(self):
        self.instance.set_hp(-1)
        self.assertTrue(self.instance.hp_less_than_zero())

    def test_hp_less_than_zero_positive(self):
        self.instance.set_hp(5)
        self.assertTrue(not self.instance.hp_less_than_zero())

    def test_hp_more_than_zero_zero(self):
        self.instance.set_hp(0)
        self.assertTrue(not self.instance.hp_more_than_zero())

    def test_hp_more_than_zero_positive(self):
        self.instance.set_hp(5)
        self.assertTrue(self.instance.hp_more_than_zero())

    def test_hp_more_than_zero_negative(self):
        self.instance.set_hp(-1)
        self.assertTrue(not self.instance.hp_more_than_zero())

    def test_add_one_to_hp(self):
        self.instance.set_hp(5)
        self.instance.add_one_to_hp()
        self.assertEqual(self.instance.get_hp(), 6)

    def test_hp_btw_zero_n_ten_zero(self):
        self.instance.set_hp(0)
        self.assertTrue(not self.instance.hp_btw_zero_n_ten())

    def test_hp_btw_zero_n_ten_ten(self):
        self.instance.set_hp(10)
        self.assertTrue(not self.instance.hp_btw_zero_n_ten())

    def test_hp_btw_zero_n_ten_five(self):
        self.instance.set_hp(5)
        self.assertTrue(self.instance.hp_btw_zero_n_ten())
