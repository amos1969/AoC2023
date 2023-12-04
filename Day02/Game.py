from Hand import Hand


class Game:
    def __init__(self, game_entry):
        game, hands = game_entry.split(":")
        self.number = int(game[5:])
        hands = hands.split(";")
        self.possible = False
        self.process_hands(hands)
        self.min_red = 0
        self.min_blue = 0
        self.min_green = 0
        self.power_of_cubes = 0
        self.get_minimums()
        self.set_power()


    def process_hands(self, hands):
        self.processed_hands = []
        for hand in hands:
            self.processed_hands.append(Hand(hand))
        is_valid = True
        for hand in self.processed_hands:
            if not hand.valid:
                is_valid = False
        self.possible = is_valid

    def get_minimums(self):
        for hand in self.processed_hands:
            if hand.red > self.min_red:
                self.min_red = hand.red
            if hand.blue > self.min_blue:
                self.min_blue = hand.blue
            if hand.green > self.min_green:
                self.min_green = hand.green

    def set_power(self):
        self.power_of_cubes = self.min_red * self.min_blue * self.min_green
        


if __name__ == "__main__":
    game_1 = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    print(game_1.power_of_cubes)
    game_2 = Game("Game 400: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")