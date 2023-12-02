from Hand import Hand


class Game:
    def __init__(self, game_entry):
        game, hands = game_entry.split(":")
        self.number = int(game[5:])
        hands = hands.split(";")
        processed_hands = []
        for hand in hands:
            processed_hands.append(Hand(hand))
        for hand in processed_hands:
            print(hand.valid)



if __name__ == "__main__":
    game_1 = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    game_2 = Game("Game 400: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")