class Mapping:
    def __init__(self, ranges):
        self.destination_start, self.source_start, self.range_length = ranges.split(" ")
        self.destination_start = int(self.destination_start)
        self.source_start = int(self.source_start)
        self.range_length = int(self.range_length)
        self.destination_end = self.destination_start + self.range_length - 1
        self.source_end = self.source_start + self.range_length - 1

    def __repr__(self):
        return f"{self.source_start} -> {self.destination_start} \n...\n{self.source_end} -> {self.destination_end}\n"

    def contains(self, value):
        return self.source_start <= value <= self.source_end

    def get_map(self, value):
        offset = value - self.source_start
        return self.destination_start + offset

if __name__ == "__main__":
    mapping1 = Mapping("50 98 2")
    mapping2 = Mapping("52 50 48")
    print(mapping2)
    print(mapping2.contains(79))
    print(mapping2.get_map(79))
