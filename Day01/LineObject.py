class LineObject:
    def __init__(self, line):
        self.words_as_numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                                 "six": "6", "seven": "7", "eight": "8", "nine": "9"}
        self.line = line
        self.registered_numbers = dict()
        self.register_numeric_words()
        self.digits = []
        self.collect_digits()
        self.extracted_number = 0
        self.generate_first_and_last_number()


    def collect_digits(self):
        for index, letter in enumerate(self.line):
            if letter.isdigit():
                self.digits.append(letter)
            elif index in self.registered_numbers:
                self.digits.append(self.registered_numbers[index])

    def generate_first_and_last_number(self):
        string_number = self.digits[0] + self.digits[-1]
        self.extracted_number = int(string_number)

    def register_numeric_words(self):
        for word in self.words_as_numbers:
            if word in self.line:
                word_positions = list(self.find_all(word))
                for position in word_positions:
                    self.registered_numbers[position] = self.words_as_numbers[word]

    def find_all(self, word):
        start = 0
        while True:
            start = self.line.find(word, start)
            if start == -1:
                return
            yield start
            start += 1

if __name__ == "__main__":

    test_1 = LineObject("twothreefour")
    test_2 = LineObject("eightwoeight56")