class Tile:
    def __init__(self, value, column, row, entry_direction=None):
        self.value = value
        self.starting_point = False
        self.column = column
        self.row = row
        self.pipes = {
            "|": ("north", "south"),
            "-": ("west", "east"),
            "L": ("north", "east"),
            "J": ("west", "north"),
            "7": ("west", "south"),
            "F": ("south", "east"),
            ".": ()
        }
        self.connections = {"north": False, "east": False, "south": False, "west": False}
        if self.value != ".":
            self.entry = entry_direction
            self.exit = None
            self.set_connections()
            self.next = ()
            self.set_next()

    def set_connections(self):
        if self.value == "S":
            self.starting_point = True
        else:
            directions = self.pipes[self.value]
            if directions:
                self.connections[directions[0]] = True
                self.connections[directions[1]] = True
                if directions[0] == self.entry:
                    self.exit = directions[1]
                else:
                    self.exit = directions[0]

    def set_starting_connections(self, first, second):
        self.connections[first] = True
        self.connections[second] = True
        self.exit = first
        self.entry = second
        self.set_next()

    def set_next(self):
        if self.exit == "north":
            self.next = (self.column, self.row - 1)
        elif self.exit == "east":
            self.next = (self.column + 1, self.row)
        elif self.exit == "south":
            self.next = (self.column, self.row + 1)
        elif self.exit == "west":
            self.next = (self.column - 1, self.row)

    def __repr__(self):
        return f"({self.column}, {self.row})"

if __name__ == "__main__":
    point_1 = Tile("S", 4, 5)
    point_1.set_starting_connections("north", "east")
    print(f"{point_1.value} - {point_1.starting_point} - Exit: {point_1.exit} - Next: {point_1.next}")

    point_2 = Tile("L", 1, 2, "north")
    print(f"{point_2.value} - {point_2.starting_point} - Exit: {point_2.exit} - Next: {point_2.next}")