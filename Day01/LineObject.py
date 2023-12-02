class LineObject:
    def __init__(self, line):
        self.line = line
        self.digits = []
        self.collect_digits()
        self.extracted_number = 0
        self.generate_first_and_last_number()


    def collect_digits(self):
        for letter in self.line:
            if letter.isdigit():
                self.digits.append(letter)

    def generate_first_and_last_number(self):
        string_number = self.digits[0] + self.digits[-1]
        self.extracted_number = int(string_number)


if __name__ == "__main__":
    test_1 = LineObject("this1isthe2")
    test_2 = LineObject("hello7isn't")