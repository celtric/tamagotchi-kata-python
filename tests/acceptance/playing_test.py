import unittest

from src.tamagotchi import *
from tests.acceptance.utils import NullClock


class PlayingTest(unittest.TestCase):

    def test_playing_with_it_increases_its_happiness(self):
        tamagotchi = self.bored_tamagotchi()
        tamagotchi.play()

        self.assertTrue(tamagotchi.is_happier_than(self.bored_tamagotchi()))

    def test_playing_with_it_increases_its_tiredness(self):
        tamagotchi = self.bored_tamagotchi()
        tamagotchi.play()

        self.assertTrue(tamagotchi.is_more_tired_than(self.bored_tamagotchi()))

    # ---[ Helpers ]-------------------------------------------------------------------- #

    def bored_tamagotchi(self):
        return Tamagotchi(NullClock())
