import unittest

from src.tamagotchi import *
from tests.acceptance.utils import FakeClock


class ChangingNeedsTest(unittest.TestCase):

    def setUp(self):
        self.clock = FakeClock()

    def test_its_tiredness_increases_over_time(self):
        tamagotchi = self.base_tamagotchi()

        self.time_passes()

        self.assertTrue(tamagotchi.is_more_tired_than(self.base_tamagotchi()))

    def test_its_hungriness_increases_over_time(self):
        tamagotchi = self.base_tamagotchi()

        self.time_passes()

        self.assertTrue(tamagotchi.is_hungrier_than(self.base_tamagotchi()))

    def test_its_happiness_decreases_over_time(self):
        tamagotchi = self.base_tamagotchi()

        self.time_passes()

        self.assertTrue(self.base_tamagotchi().is_happier_than(tamagotchi))

    # ---[ Helpers ]-------------------------------------------------------------------- #

    def base_tamagotchi(self):
        tamagotchi = Tamagotchi(self.clock)
        tamagotchi.start()
        return tamagotchi

    def time_passes(self):
        self.clock.pass_time()
