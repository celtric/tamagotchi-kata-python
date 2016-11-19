import unittest

from src.tamagotchi import *
from tests.acceptance.utils import NullClock


class FeedingTest(unittest.TestCase):

    def test_feeding_it_decreases_its_hungriness(self):
        tamagotchi = self.hungry_tamagotchi()
        tamagotchi.feed()

        self.assertTrue(self.hungry_tamagotchi().is_hungrier_than(tamagotchi))

    def test_feeding_it_increases_its_fullness(self):
        tamagotchi = self.hungry_tamagotchi()
        tamagotchi.feed()

        self.assertTrue(tamagotchi.is_fuller_than(self.hungry_tamagotchi()))

    # ---[ Helpers ]-------------------------------------------------------------------- #

    def hungry_tamagotchi(self):
        return Tamagotchi(NullClock())
