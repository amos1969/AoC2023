from Hand import Hand

class Game:
    def __init__(self, game_data):
        self.hands = []
        self.load_hands(game_data)
        self.hands.sort()
        self.total_winnings = 0
        self.calculate_winnings()


    def load_hands(self, game_data):
        with open(game_data, "r") as the_file:
            for line in the_file:
                line = line.strip()
                self.hands.append(Hand(line))

    def calculate_winnings(self):
        for index, hand in enumerate(self.hands):
            self.total_winnings += (index + 1) * hand.bid

if __name__ == "__main__":
    game = Game("input.txt")
    print(game.total_winnings)