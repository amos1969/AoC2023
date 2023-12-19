from Empty import Empty
from Mirror import Mirror
from Splitter import Splitter
import copy

class Contraption:
    def __init__(self, contraption_data):
        self.initial_contraption_map = []
        self.load_data(contraption_data)
        self.highest_energy = 0
        self.beam_start_points = []
        self.generate_beams()
        self.energised_tile_scores = []
        for a_beam in self.beam_start_points:
            self.beam = [a_beam]

            self.contraption_map = copy.deepcopy(self.initial_contraption_map)
            self.beam_history = []
            while self.beam:
                self.zap()
            self.energised_tile_scores.append(self.count_energised_tiles())
        self.highest_energy = max(self.energised_tile_scores)

    def load_data(self, contraption_data):
        with open(contraption_data, "r") as the_file:
            for row, line in enumerate(the_file):
                horizontal_row = []
                line = line.strip()
                for column, tile in enumerate(line):
                    if tile == ".":
                        horizontal_row.append(Empty(column, row))
                    elif tile == "/" or tile == "\\":
                        horizontal_row.append(Mirror(column, row, tile))
                    elif tile == "-" or tile == "|":
                        horizontal_row.append(Splitter(column, row, tile))
                self.initial_contraption_map.append(horizontal_row)

    def zap(self):
        new_beams = []
        for beam_end in self.beam:
            column, row, direction = beam_end
            if beam_end not in self.beam_history:
                self.beam_history.append(beam_end)
                if 0 <= column <= len(self.contraption_map[0]) - 1:
                    if 0 <= row <= len(self.contraption_map) - 1:
                        tile = self.contraption_map[row][column]
                        beams = tile.get_next_tile(direction)
                        for beam in beams:
                            new_beams.append(beam)
        self.beam = new_beams[:]

    def count_energised_tiles(self):
        number_of_energised_tiles = 0
        for row in self.contraption_map:
            for tile in row:
                if tile.energised:
                    number_of_energised_tiles += 1
        return number_of_energised_tiles

    def generate_beams(self):
        bottom_row = len(self.initial_contraption_map) - 1
        right_column = len(self.initial_contraption_map[0]) - 1
        for x in range(len(self.initial_contraption_map[0])):
            self.beam_start_points.append((x, 0, "down"))
            self.beam_start_points.append((x, bottom_row, "up"))
        for y in range(len(self.initial_contraption_map)):
            self.beam_start_points.append((0, y, "right"))
            self.beam_start_points.append((right_column, y, "left"))


if __name__ == "__main__":
     contraption = Contraption("input.txt")
     print(contraption.highest_energy)
