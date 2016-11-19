class Tamagotchi:

    def __init__(self):
        self.fullness = 0
        self.happiness = 0
        self.hungriness = 0
        self.tiredness = 0

    def feed(self):
        self.hungriness -= 1
        self.fullness += 1

    def play(self):
        self.happiness += 1
        self.tiredness += 1

    def is_hungrier_than(self, another_tamagotchi) -> bool:
        return self.hungriness > another_tamagotchi.hungriness

    def is_fuller_than(self, another_tamagotchi) -> bool:
        return self.fullness > another_tamagotchi.fullness

    def is_happier_than(self, another_tamagotchi):
        return self.happiness > another_tamagotchi.happiness

    def is_more_tired_than(self, another_tamagotchi):
        return self.tiredness > another_tamagotchi.tiredness
