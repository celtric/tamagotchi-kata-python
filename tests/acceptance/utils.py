from src.tamagotchi import Clock


class NullClock(Clock):
    pass


class FakeClock(Clock):

    def pass_time(self):
        for callback in self.callbacks:
            callback()
