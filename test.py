import random

class Dice:
    def roll(self):
        first = random.randint(1, 8)
        second = random.randint(1, 8)
        return first, second


dice = Dice()
print(dice.roll())
