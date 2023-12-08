from Node import Node
from math import lcm

class Chart:
    def __init__(self, map_data):
        self.left_right = ""
        self.rows = dict()
        self.load_data(map_data)
        self.current_nodes = []
        self.get_starting_points()
        self.step_totals = []
        self.walk_map()
        print(lcm(*self.step_totals))

    def get_starting_points(self):
        for row in self.rows:
            if row[2] == "A":
                self.current_nodes.append(row)

    def walk_map(self):
        current_node = ""
        for node in self.current_nodes:
            current_node = node
            current_lr_position = 0
            steps = 0
            next_node = ""
            while current_node[2] != "Z":
                if current_lr_position >= len(self.left_right):
                    current_lr_position = 0
                if self.left_right[current_lr_position] == "L":
                    next_node = self.rows[current_node].left
                else:
                    next_node = self.rows[current_node].right
                current_node = next_node
                current_lr_position += 1
                steps += 1
            self.step_totals.append(steps)

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
