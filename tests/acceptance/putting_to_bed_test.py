import unittest

from src.tamagotchi import *


class PuttingToBedTest(unittest.TestCase):

    def test_putting_it_to_bed_decreases_its_tiredness(self):
        tamagotchi = self.base_tamagotchi()
        tamagotchi.put_to_bed()

        self.assertTrue(self.base_tamagotchi().is_more_tired_than(tamagotchi))

    # ---[ Helpers ]-------------------------------------------------------------------- #

    def base_tamagotchi(self):
        return Tamagotchi()
