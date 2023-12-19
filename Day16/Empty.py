from Tile import Tile

class Empty(Tile):
    def __init__(self, column, row):
        super().__init__(column, row)
        self.symbol = "."

    def get_next_tile(self, direction):
        self.energise()
        if direction == "down":
            return [(self.column, self.row + 1, direction)]
        elif direction == "right":
            return [(self.column + 1, self.row, direction)]
        elif direction == "up":
            return [(self.column, self.row - 1, direction)]
        elif direction == "left":
            return [(self.column - 1, self.row, direction)]

    def __repr__(self):
        return self.symbol