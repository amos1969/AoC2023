from Node import Node

class Chart:
    def __init__(self, map_data):
        self.left_right = ""
        self.rows = dict()
        self.steps = 0
        self.path = ""
        self.load_data(map_data)
        self.walk_map()

    def walk_map(self):
        current_node = "AAA"
        current_lr_position = 0
        next_node = ""
        self.path = "AAA"
        while current_node != "ZZZ":
            if current_lr_position >= len(self.left_right):
                current_lr_position = 0
            if self.left_right[current_lr_position] == "L":
                next_node = self.rows[current_node].left
            else:
                next_node = self.rows[current_node].right
            current_node = next_node
            self.path += " -> " + current_node
            current_lr_position += 1
            self.steps += 1

    def load_data(self, map_data):
        with open(map_data, "r") as the_file:
            first_line = True
            for line in the_file:
                line = line.strip()
                if first_line:
                    first_line = False
                    self.left_right = line
                else:
                    if line:
                        node = Node(line)
                        self.rows[node.element] = node


if __name__ == "__main__":
    chart_1 = Chart("input.txt")
    print(chart_1.path)
    print(chart_1.steps)
