from player import Player
from space import Space
from dice import Dice

class Simulator:
    lands = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0]

    # place = Space()

    def play(self, iterations): # simulates turns in isolation
        player = Player()
        for i in range(0, iterations):
            player.current_space.current_place += Dice.roll(12)
            if player.current_space.current_place > 39:
                player.current_space.current_place -= 40
            self.lands[player.current_space.current_place] += 1
            player.current_space.chance(player.current_space.current_place)
            player.current_space.community_chest(player.current_space.current_place)

    def play_with_players(self, games): # plays with 2 bots on opposing strategies
        bot1 = Player(True) # only buys profitable properties
        bot2 = Player() # buys all properties

        wins_bot_1 = 0
        wins_bot_2 = 0

        for i in range(0, games):
            while True:
                bot1.current_space.current_place += Dice.roll(12)
                if bot1.current_space.current_place > 39:
                    bot1.current_space.current_place -= 40
                bot1.check_buy(bot1.current_space.current_place, bot2)

                bot2.current_space.current_place += Dice.roll(12)
                if bot2.current_space.current_place > 39:
                    bot2.current_space.current_place -= 40
                bot2.check_buy(bot2.current_space.current_place, bot1)

                if bot1.current_money <= 0:
                    wins_bot_2 += 1
                    break
                elif bot2.current_money <= 0:
                    wins_bot_1 += 1
                    break
        return wins_bot_1, wins_bot_2
