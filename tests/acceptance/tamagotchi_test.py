import unittest

from src.tamagotchi import *


class TamagotchiTest(unittest.TestCase):

    def test_feeding_it_decreases_its_hungriness(self):
        tamagotchi = self.base_tamagotchi()
        tamagotchi.feed()

        self.assertTrue(self.base_tamagotchi().is_hungrier_than(tamagotchi))

    def test_feeding_it_increases_its_fullness(self):
        tamagotchi = self.base_tamagotchi()
        tamagotchi.feed()

        self.assertTrue(tamagotchi.is_fuller_than(self.base_tamagotchi()))

    # ---[ Helpers ]-------------------------------------------------------------------- #

    def base_tamagotchi(self):
        return Tamagotchi()
