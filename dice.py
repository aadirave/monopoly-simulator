import random


class Dice:
    def roll(faces):
        result = random.randint(1, faces)
        return result
