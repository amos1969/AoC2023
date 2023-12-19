from Tile import Tile

class Mirror(Tile):
    def __init__(self, column, row, symbol):
        super().__init__(column, row)
        self.symbol = symbol

    def get_next_tile(self, direction):
        self.energise()
        if self.symbol == "/":
            if direction == "down":
                return [(self.column - 1, self.row, "left")]
            elif direction == "right":
                return [(self.column, self.row - 1, "up")]
            elif direction == "up":
                return [(self.column + 1, self.row, "right")]
            elif direction == "left":
                return [(self.column, self.row + 1, "down")]
        elif self.symbol == "\\":
            if direction == "down":
                return [(self.column + 1, self.row, "right")]
            elif direction == "right":
                return [(self.column, self.row + 1, "down")]
            elif direction == "up":
                return [(self.column - 1, self.row, "left")]
            elif direction == "left":
                return [(self.column, self.row - 1, "up")]

    def __repr__(self):
        return self.symbol