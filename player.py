class Player:
    current_money = 1500
    current_space = Space()
    is_owned = [False, False, False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False, False, False, False, False,
                False, False, False]
    buy_profitable = False

    def __init__(self, strategy=False):
        Player.buy_profitable = strategy

    def set_ownership(self, place_no, to_set):
        self.is_owned[place_no] = to_set

    def check_ownership(self, place_no):
        if self.is_owned[place_no]:
            return True
        else:
            return False

    def pay_rent(self, place_no, player2):
        self.current_money -= Space.rent[place_no]
        player2.current_money += Space.rent[place_no]

    def check_buy(self, place_no, player2):
        if player2.check_ownership(place_no):
            self.pay_rent(self.current_space.current_place, player2)
            return
        elif self.current_money > Space.price[place_no] and self.buy_profitable == False:
            self.set_ownership(place_no, True)
            self.current_money -= Space.price[place_no]
        elif self.current_money > Space.price[place_no] and self.buy_profitable == True:
            simulate = Simulator()
            simulate.play(50)
            if simulate.lands[place_no] * Space.rent[place_no] > Space.price[place_no]:
                self.set_ownership(place_no, True)
                self.current_money -= Space.price[place_no]
        else:
            return