class Tile:
    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.energised = False
        self.energy = 0

    def get_next_tile(self, direction):
        pass

    def energise(self):
        self.energised = True
        self.energy += 1