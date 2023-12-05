from Symbol import Symbol
from Cell import Cell
from Number import Number

class Schematic:
    def __init__(self, schematic_data):
        self.numbers = []
        self.symbols = []
        self.parse_schematic(schematic_data)
        self.part_numbers = []
        self.find_parts()
        self.parts_total = 0
        self.calculate_parts_total()
        self.gear_ratio_total = 0
        self.find_gears()

    def parse_schematic(self, schematic_data):
        with open(schematic_data, "r") as the_file:
            for row, line in enumerate(the_file):
                line = line.strip()
                digits = ""
                positions = []
                for column, symbol in enumerate(line):
                    if symbol != ".":
                        if symbol.isdigit():
                            digits = digits + symbol
                            positions.append(Cell(column, row))
                        else:
                            self.symbols.append(Symbol(symbol, Cell(column, row)))
                            if digits:
                                self.numbers.append(Number(int(digits), positions))
                                digits = ""
                                positions = []
                    else:
                        if digits:
                            self.numbers.append(Number(int(digits), positions))
                            digits = ""
                            positions = []
                if digits:
                    self.numbers.append(Number(int(digits), positions))


    def find_parts(self):
        for number in self.numbers:
            for symbol in self.symbols:
                if number.check_if_bordering(symbol.position):
                    self.part_numbers.append(number.value)

    def find_gears(self):
        potential_gears = []
        for symbol in self.symbols:
            if symbol.symbol == "*":
                potential_gears.append(symbol)
        for symbol in potential_gears:
            gears = []
            for number in self.numbers:
                if number.check_if_bordering(symbol.position):
                    gears.append(number)
            if len(gears) == 2:
                self.gear_ratio_total += gears[0].value * gears[1].value


    def calculate_parts_total(self):
        self.parts_total = 0
        for part in self.part_numbers:
            self.parts_total += part

if __name__ == "__main__":
    schematic = Schematic("input.txt")
    print(schematic.gear_ratio_total)