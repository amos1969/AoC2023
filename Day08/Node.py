class Node:
    def __init__(self, row_data):
        self.element = row_data[:3]
        self.left = row_data[7:10]
        self.right = row_data[12:15]
        self.starter = False
        self.ender = False
        if self.element[2] == "A":
            self.starter = True
        if self.element[2] == "Z":
            self.ender = True

    def __repr__(self):
        return f"{self.element} - ({self.left}, {self.right})"


if __name__ == "__main__":
    node_1 = Node("AAA = (BBB, CCC)")