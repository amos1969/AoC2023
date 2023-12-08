class Node:
    def __init__(self, row_data):
        self.element = row_data[:3]
        self.left = row_data[7:10]
        self.right = row_data[12:15]

    def is_start(self):
        return self.element == "AAA"

    def is_end(self):
        return self.element == "ZZZ"

    def __repr__(self):
        return f"{self.element} - ({self.left}, {self.right})"


if __name__ == "__main__":
    node_1 = Node("AAA = (BBB, CCC)")