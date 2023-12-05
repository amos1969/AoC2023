class Cell:
    def __init__(self, column, row):
        self.column = column
        self.row = row

    def __repr__(self):
        return f"(col: {self.column}, row: {self.row})"

    def __eq__(self, other):
        return (self.column, self.row) == (other.column, other.row)

    def __hash__(self):
        return hash(f"(col: {self.column}, row: {self.row})")