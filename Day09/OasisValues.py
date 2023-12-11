from Sequence import Sequence

class OasisValues:
    def __init__(self, oasis_data):
        self.sequences = []
        self.load_data(oasis_data)
        self.total = 0
        self.extrapolated_total = 0
        self.get_totals()
        self.get_extrapolated_totals()

    def load_data(self, oasis_data):
        with open(oasis_data, "r") as the_file:
            for line in the_file:
                line = line.strip()
                self.sequences.append(Sequence(line))

    def get_totals(self):
        for sequence in self.sequences:
            self.total += sequence.next_value

    def get_extrapolated_totals(self):
        for sequence in self.sequences:
            self.extrapolated_total += sequence.extrapolated_value


if __name__ == "__main__":
    oasis_values = OasisValues("input.txt")
    print(oasis_values.extrapolated_total)