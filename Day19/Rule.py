from Part import Part

class Rule:
    def __init__(self, rule):
        self.raw_rule = rule
        self.letter = rule[:1]
        self.symbol = rule[1:2]
        self.value, self.destination = rule[2:].split(":")
        self.value = int(self.value)

    def check_rule(self, part):
        success = False
        destination = ""
        part_value = None
        if self.letter == "x":
            part_value = part.x
        elif self.letter == "m":
            part_value = part.m
        elif self.letter == "a":
            part_value = part.a
        elif self.letter == "s":
            part_value = part.s
        if self.symbol == "<":
            if part_value < self.value:
                success = True
                destination = self.destination
        elif self.symbol == ">":
            if part_value > self.value:
                success = True
                destination = self.destination
        return success, destination

    def __repr__(self):
        return f"{self.letter} {self.symbol} {self.value} -> {self.destination}"

if __name__ == "__main__":
    rule = Rule("a<2006:qkq")
    print(f"Letter: {rule.letter}")
    print(f"Symbol: {rule.symbol}")
    print(f"Value: {rule.value}")
    print(f"Destination: {rule.destination}")