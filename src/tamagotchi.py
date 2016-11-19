class Tamagotchi:

    def __init__(self):
        self.fullness = 0
        self.hungriness = 0

    def feed(self):
        self.hungriness -= 1
        self.fullness += 1

    def is_hungrier_than(self, another_tamagotchi) -> bool:
        return self.hungriness > another_tamagotchi.hungriness

    def is_fuller_than(self, another_tamagotchi) -> bool:
        return self.fullness > another_tamagotchi.fullness
