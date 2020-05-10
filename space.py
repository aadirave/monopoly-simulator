class Space:
    place_names = ['Old Kent Road', 'Community Chest', 'Whitechapel Road',
                   'Income Tax', 'Kings Cross Station', 'The Angel, Islington', 'Chance', 'Euston Road',
                   'Pentonville Road', 'Just Visiting', 'Pall Mall', 'Electric Company', 'Whitehall',
                   'Northumberland Avenue', 'Marylebone Station', 'Bow Street', 'Community Chest',
                   'Marlborough Street', 'Vine Street', 'Free Parking', 'Strand', 'Chance',
                   'Fleet Street', 'Trafalgar Square', 'Fenchurch Station', 'Leicester Square',
                   'Coventry Street', 'Water Works', 'Piccadily', 'Jail', 'Regent Street',
                   'Oxford Street', 'Community Chest', 'Bond Street', 'Liverpool Station', 'Chance',
                   'Park Lane', 'Super Tax', 'Mayfair', 'GO']
    place_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                     27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
    community_chest = [1, 16, 32]
    chance = [6, 21, 35]
    rent = [2, 0, 4, 0, 50, 6, 0, 6, 8, 0, 10, 0, 10, 12, 50, 14, 0, 14, 16, 0, 18,
            0, 18, 20, 50, 22, 22, 0, 22, 0, 26, 26, 0, 28, 50, 0, 35, 0, 50, 0]
    price = [60, 0, 60, 200, 200, 100, 0, 100, 120, 0, 140, 150, 0, 140, 160, 200,
             180, 0, 180, 200, -50, 220, 0, 220, 240, 200, 260, 260, 0, 280, 50, 300,
             300, 0, 320, 200, 0, 350, 100, 400, -200]
    current_place = 0

    @staticmethod
    def chance(current_place):
        if current_place == Space.chance[0] or current_place == Space.chance[1] or current_place == Space.chance[2]:
            if Dice.roll(16) == 1:
                return 24
            elif Dice.roll(16) == 2:
                return 39
            elif Dice.roll(16) == 3:
                return 5
            elif Dice.roll(16) == 4:
                return 11
            elif Dice.roll(16) == 5:
                return 0
            elif Dice.roll(16) == 6:
                return 30
            else:
                return current_place
        return current_place

    @staticmethod
    def community_chest(current_place):
        if current_place == Space.community_chest[0] or current_place == Space.community_chest[1] or current_place == \
                Space.community_chest[2]:
            if Dice.roll(16) == 1:
                return 0
            elif Dice.roll(16) == 2:
                return 30
            else:
                return current_place
        return current_place
