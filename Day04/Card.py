class Card:
    def __init__(self, card_data):
        card_number, numbers = card_data.split(":")
        self.number = int(card_number[5:].strip())
        winning_numbers, my_numbers = numbers.split("|")
        winning_numbers = winning_numbers.strip()
        my_numbers = my_numbers.strip()
        self.winning_numbers = []
        for number in winning_numbers.split(" "):
            if number:
                self.winning_numbers.append(int(number))
        self.my_numbers = []
        for number in my_numbers.split(" "):
            if number:
                self.my_numbers.append(int(number))
        self.score = 0
        self.wins = 0
        self.calculate_winning_score()

    def calculate_winning_score(self):
        wins = 0
        for number in self.winning_numbers:
            if number in self.my_numbers:
                wins += 1
        if wins:
            self.score = 2**(wins-1)
        self.wins = wins
