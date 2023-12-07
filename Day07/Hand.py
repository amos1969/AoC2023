import collections
class Hand:
    def __init__(self, hand_data):
        self.card_ordering = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 1,
            "T": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2
        }
        self.hand_type_ordering = {
            "Five of a Kind": 7,
            "Four of a Kind": 6,
            "Full House": 5,
            "Three of a Kind": 4,
            "Two Pairs": 3,
            "One Pair": 2,
            "High Card": 1
        }
        self.hand, self.bid = hand_data.split(" ")
        self.bid = int(self.bid)
        self.tie_break_hand = self.hand
        self.deal_with_jokers()
        self.hand_type = ""
        self.calculate_hand_type()

    def calculate_hand_type(self):
        cards = collections.defaultdict(int)
        for card in self.hand:
            cards[card] += 1
        number_of_distinct_cards = len(cards)
        if number_of_distinct_cards == 5:
            self.hand_type = "High Card"
        elif number_of_distinct_cards == 4:
            self.hand_type = "One Pair"
        elif number_of_distinct_cards == 3:
            if 3 in list(cards.values()):
                self.hand_type = "Three of a Kind"
            else:
                self.hand_type = "Two Pairs"
        elif number_of_distinct_cards == 2:
            if 2 in list(cards.values()):
                self.hand_type = "Full House"
            else:
                self.hand_type = "Four of a Kind"
        elif number_of_distinct_cards == 1:
            self.hand_type = "Five of a Kind"

    def deal_with_jokers(self):
        if "J" in self.hand:
            position_of_first_j = self.hand.rfind("J")
            cards = collections.defaultdict(int)
            for card in self.hand:
                cards[card] += 1
            number_of_distinct_cards = len(cards)
            if number_of_distinct_cards == 1:
                return
            else:
                del cards["J"]
                card_name = max(cards, key = lambda key: cards[key])
                self.hand = self.hand[:position_of_first_j] + card_name + self.hand[position_of_first_j+1:]
            self.deal_with_jokers()


    def __lt__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type_ordering[self.hand_type] < self.hand_type_ordering[other.hand_type]
        else:
            for index in range(len(self.tie_break_hand)):
                if self.tie_break_hand[index] != other.tie_break_hand[index]:
                    return self.card_ordering[self.tie_break_hand[index]] < self.card_ordering[other.tie_break_hand[index]]

    def __gt__(self, other):
        return other < self

    def __repr__(self):
        return f"{self.hand} - {self.hand_type} - {self.bid}"


if __name__ == "__main__":
    # hand1 = Hand("32T3K 765")
    # hand2 = Hand("T55J5 684")
    # hand3 = Hand("KK677 28")
    # hand4 = Hand("KTJJT 220")
    # hand5 = Hand("QQQJA 483")
    # hand6 = Hand("T44T4 23")
    # hand7 = Hand("T4444 23")
    # hand8 = Hand("T1234 23")
    # print(hand4 < hand5)
    hand1 =  Hand("AAAJA 234")
    print(hand1)
    hand2 = Hand("JJJJA 234")
    print(hand2)