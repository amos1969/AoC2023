from Card import Card
class PileOfCards:
    def __init__(self, game_data):
        self.cards = []
        with open(game_data, "r") as the_file:
            for line in the_file:
                line = line.strip()
                self.cards.append(Card(line))
        self.grand_total = 0
        self.card_record = dict()
        for card in self.cards:
            self.grand_total += card.score
            self.card_record[card.number] = 1
        for card in self.cards:
            wins = card.wins
            number_of_current_cards = self.card_record[card.number]
            for i in range(1, wins+1):
                self.card_record[card.number + i] += number_of_current_cards
        self.total_number_of_cards = 0
        for card in self.card_record.keys():
            self.total_number_of_cards += self.card_record[card]




if __name__ == "__main__":
    game = PileOfCards("input.txt")
    print(game.total_number_of_cards)