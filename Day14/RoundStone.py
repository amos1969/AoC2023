class RoundStone:
    def __init__(self, column, row):
        self.current_row = row
        self.current_column = column
        self.can_move = True

    def move_up(self):
        self.current_row -= 1


