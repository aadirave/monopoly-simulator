import random

class Dice: # dice simulation
    def roll(faces = 12): # simulates rolling dice
        result = random.randint(1, faces)
        return result
