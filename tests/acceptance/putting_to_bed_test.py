import unittest

from src.tamagotchi import *
from tests.acceptance.utils import NullClock


class PuttingToBedTest(unittest.TestCase):

    def test_putting_it_to_bed_decreases_its_tiredness(self):
        tamagotchi = self.tired_tamagotchi()
        tamagotchi.put_to_bed()

        self.assertTrue(self.tired_tamagotchi().is_more_tired_than(tamagotchi))

    # ---[ Helpers ]-------------------------------------------------------------------- #

    def tired_tamagotchi(self):
        return Tamagotchi(NullClock())
