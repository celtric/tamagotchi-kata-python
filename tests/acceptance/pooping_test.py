import unittest

from src.tamagotchi import *
from tests.acceptance.utils import NullClock


class PoopingTest(unittest.TestCase):

    def test_making_it_poop_decreases_its_fullness(self):
        tamagotchi = self.full_tamagotchi()
        tamagotchi.make_poop()

        self.assertTrue(self.full_tamagotchi().is_fuller_than(tamagotchi))

    # ---[ Helpers ]-------------------------------------------------------------------- #

    def full_tamagotchi(self):
        return Tamagotchi(NullClock())
