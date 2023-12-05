from Cell import Cell
from Symbol import Symbol

class Number:
    def __init__(self, value, positions):
        self.value = value
        self.positions = positions
        self.border = set()
        self.set_border()


    def set_border(self):
        for cell in self.positions:
            self.border = self.border.union({
                Cell(cell.column - 1, cell.row - 1),
                Cell(cell.column, cell.row - 1),
                Cell(cell.column + 1, cell.row - 1),
                Cell(cell.column - 1, cell.row),
                Cell(cell.column + 1, cell.row),
                Cell(cell.column - 1, cell.row + 1),
                Cell(cell.column, cell.row + 1),
                Cell(cell.column + 1, cell.row + 1)
            })
        self.border = self.border.difference(set(self.positions))

    def __repr__(self):
        return f"Number: {self.value} at: {self.positions}."

    def check_if_bordering(self, position):
        for cell in self.border:
            if cell == position:
                return True
        return False

if __name__ == "__main__":
    number = Number(234, [Cell(3, 1), Cell(4, 1), Cell(5, 1)])
    number2 = Number(4, [Cell(0,0)])
    symbol = Symbol("*", Cell(6, 0))
    print(number2.check_if_bordering(symbol.position))