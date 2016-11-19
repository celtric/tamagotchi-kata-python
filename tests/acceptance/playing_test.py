import unittest

from src.tamagotchi import *


class PlayingTest(unittest.TestCase):

    def test_playing_with_it_increases_its_happiness(self):
        tamagotchi = self.base_tamagotchi()
        tamagotchi.play()

        self.assertTrue(tamagotchi.is_happier_than(self.base_tamagotchi()))

    def test_playing_with_it_increases_its_tiredness(self):
        tamagotchi = self.base_tamagotchi()
        tamagotchi.play()

        self.assertTrue(tamagotchi.is_more_tired_than(self.base_tamagotchi()))

    # ---[ Helpers ]-------------------------------------------------------------------- #

    def base_tamagotchi(self):
        return Tamagotchi()
