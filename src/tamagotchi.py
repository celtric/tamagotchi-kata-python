class Tamagotchi:

    def __init__(self, clock):
        self.clock = clock
        self.fullness = 0
        self.happiness = 0
        self.hungriness = 0
        self.tiredness = 0

    def start(self):
        self.clock.on_time_pass(lambda: self.time_passed())

    def feed(self):
        self.hungriness -= 1
        self.fullness += 1

    def play(self):
        self.happiness += 1
        self.tiredness += 1

    def put_to_bed(self):
        self.tiredness -= 1

    def make_poop(self):
        self.fullness -= 1

    def is_hungrier_than(self, another_tamagotchi) -> bool:
        return self.hungriness > another_tamagotchi.hungriness

    def is_fuller_than(self, another_tamagotchi) -> bool:
        return self.fullness > another_tamagotchi.fullness

    def is_happier_than(self, another_tamagotchi) -> bool:
        return self.happiness > another_tamagotchi.happiness

    def is_more_tired_than(self, another_tamagotchi) -> bool:
        return self.tiredness > another_tamagotchi.tiredness

    def time_passed(self):
        self.tiredness += 1
        self.hungriness += 1
        self.happiness -= 1


class Clock:

    def __init__(self):
        self.callbacks = []

    def on_time_pass(self, callback):
        self.callbacks.append(callback)
