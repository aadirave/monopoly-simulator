from dice import Dice
from space import Space

class Player: # simulates all the characteristics of a player
    current_money = 1500 # starting money as per monopoly rules
    current_space = Space()
    is_owned = [False, False, False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False, False, False, False, False,
                False, False, False] # defines ownership of a space
    buy_profitable = False # strategy

    def __init__(self, strategy = False): # constructor
        Player.buy_profitable = strategy

    def set_ownership(self, place_no, to_set): # sets ownership to true or false
        self.is_owned[place_no] = to_set

    def check_ownership(self, place_no): # checks if the player owns said property
        if self.is_owned[place_no]:
            return True
        else:
            return False

    def pay_rent(self, place_no, player2): # pays rent to the other player
        self.current_money -= Space.rent[place_no]
        player2.current_money += Space.rent[place_no]

    def check_buy(self, place_no, player2): # checks if it is possible to buy a property and then buys it if needed
        if player2.check_ownership(place_no): # checks if the other player owns the property and pays rent if so
            self.pay_rent(self.current_space.current_place, player2)
            return
        elif self.current_money > Space.price[place_no] and self.buy_profitable == False: # checks for strategy set
            # and then buys it if there is enough money
            self.set_ownership(place_no, True)
            self.current_money -= Space.price[place_no]
        elif self.current_money > Space.price[place_no] and self.buy_profitable == True: # checks for strategy set and
            # buys it if it is profitable
            simulate = Simulator()
            simulate.play(50) # plays 50 turns ( average length of a game ) and then buys it if it is profitable
            if simulate.lands[place_no] * Space.rent[place_no] > Space.price[place_no]:
                self.set_ownership(place_no, True)
                self.current_money -= Space.price[place_no]
        else:
            return