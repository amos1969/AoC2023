class Sequence:
    def __init__(self, initial_data):
        self.sequence = []
        self.next_value = None
        self.extrapolated_value = None
        self.differences = []
        for number in initial_data.split(" "):
            self.sequence.append(int(number))
        self.get_all_differences()
        self.set_next_value()
        self.set_extrapolated_value()

    def get_differences(self, some_sequence):
        differences = []
        for i in range(len(some_sequence) - 1):
            differences.append(some_sequence[i+1] - some_sequence[i])
        return differences

    def get_all_differences(self):
        differences = self.sequence
        for i in range(len(self.sequence) - 1):
            differences = self.get_differences(differences)
            self.differences.append(differences)
            if len(set(differences)) == 1:
                break

    def set_next_value(self):
        offset = 0
        for difference_list in self.differences:
            offset += difference_list[-1]
        self.next_value = self.sequence[-1] + offset

    def set_extrapolated_value(self):
        offset = 0
        if len(self.differences)%2 == 0:
            sign = -1
        else:
            sign = 1
        for index, difference_list in enumerate(reversed(self.differences)):
            offset += sign * difference_list[0]
            sign = -sign
        self.extrapolated_value = self.sequence[0] - offset


if __name__ == "__main__":
    sequence1 = Sequence("0 3 6 9 12 15")
    print(f"{sequence1.sequence} - {sequence1.next_value}")
    print(f"{len(sequence1.differences)}")
    print(f"Extrapolated value: {sequence1.extrapolated_value}")
    sequence2 = Sequence("1 3 6 10 15 21")
    print(f"{sequence2.sequence} - {sequence2.next_value}")
    print(f"{len(sequence2.differences)}")
    print(f"Extrapolated value: {sequence2.extrapolated_value}")
    sequence3 = Sequence("10 13 16 21 30 45")
    print(f"{sequence3.sequence} - {sequence3.next_value}")
    print(f"{len(sequence3.differences)}")
    print(f"Extrapolated value: {sequence3.extrapolated_value}")

