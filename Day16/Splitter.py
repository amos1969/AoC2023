from Tile import Tile

class Splitter(Tile):
    def __init__(self, column, row, symbol):
        super().__init__(column, row)
        self.symbol = symbol

    def get_next_tile(self, direction):
        self.energise()
        if self.symbol == "-":
            if direction == "down":
                return [(self.column - 1, self.row, "left"), (self.column + 1, self.row, "right")]
            elif direction == "right":
                return [(self.column + 1, self.row, "right")]
            elif direction == "up":
                return [(self.column - 1, self.row, "left"), (self.column + 1, self.row, "right")]
            elif direction == "left":
                return [(self.column - 1, self.row, "left")]
        elif self.symbol == "|":
            if direction == "down":
                return [(self.column, self.row + 1, "down")]
            elif direction == "right":
                return [(self.column, self.row + 1, "down"), (self.column, self.row - 1, "up")]
            elif direction == "up":
                return [(self.column, self.row - 1, "up")]
            elif direction == "left":
                return [(self.column, self.row + 1, "down"), (self.column, self.row - 1, "up")]

    def __repr__(self):
        return self.symbol