# author - aadi rave
# version - 2.1
# name - monopoly-simulator
# date - 11.05.2020
# git repository - github.com/aadirave/monopoly-simulator

import math
import random
from dice import Dice
from player import Player
from simulator import Simulator
from space import Space

games = int(input('number of games to run: '))

simulate = Simulator()
wins_bot_1, wins_bot_2 = simulate.play_with_players(games)
print('bot 1 wins ' + str(wins_bot_1))
print('bot 2 wins ' + str(wins_bot_2))