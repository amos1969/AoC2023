from Tile import Tile

class TheMap:
    def __init__(self, map_data):
        self.starting_tile = (-1, -1)
        self.map = []
        self.load_data(map_data)
        self.get_starting_tile_coordinates()
        self.loop_total = 0
        self.path = []
        self.walk_the_map()
        self.updated_map = []
        self.mark_the_map()
        self.mark_interiors()
        self.rights = 0
        self.count_rights()

    def count_rights(self):
        self.rights = 0
        for line in self.updated_map:
            for square in line:
                if square == "R":
                    self.rights += 1

    def get_starting_tile_coordinates(self):
        for row, line in enumerate(self.map):
            for column, square in enumerate(line):
                if square == "S":
                    self.starting_tile = (column, row)
                    break
            else:
                continue
            break

    def load_data(self, map_data):
        with open(map_data, "r") as the_file:
            for line in the_file:
                line = line.strip()
                self.map.append(list(line))

    def set_starting_directions(self):
        values = []
        column, row = self.starting_tile
        if column != 0:
            west = self.map[row][column - 1]
            if west in ["-", "L", "F"]:
                values.append("west")
        if row != 0:
            north = self.map[row - 1][column]
            if north in ["|", "7", "F"]:
                values.append("north")
        if column < len(self.map[0]) - 1:
            east = self.map[row][column + 1]
            if east in ["-", "J", "7"]:
                values.append("east")
        if row < len(self.map) - 1:
            south = self.map[row + 1][column]
            if south in ["|", "J", "L"]:
                values.append("south")
        print(values)
        return values

    def walk_the_map(self):
        map_entry_to_exit = {"north": "south", "east": "west", "south": "north", "west": "east"}
        column, row = self.starting_tile
        current_tile = Tile(self.map[row][column], column, row)
        self.path.append((current_tile.column, current_tile.row))
        first, second = self.set_starting_directions()
        current_tile.set_starting_connections(first, second)
        next_entry = map_entry_to_exit[current_tile.exit]
        next_column, next_row = current_tile.next
        self.loop_total += 1
        current_tile = Tile(self.map[next_row][next_column], next_column, next_row, next_entry)
        self.path.append((current_tile.column, current_tile.row))
        while current_tile.value != "S":
            next_entry = map_entry_to_exit[current_tile.exit]
            next_column, next_row = current_tile.next
            self.loop_total += 1
            current_tile = Tile(self.map[next_row][next_column], next_column, next_row, next_entry)
            self.path.append((current_tile.column, current_tile.row))

    # def direct_the_map(self):
    #     map_entry_to_exit = {"north": "south", "east": "west", "south": "north", "west": "east"}
    #     column, row = self.starting_tile
    #     current_tile = Tile(self.map[row][column], column, row)
    #     first, second = self.set_starting_directions()
    #     current_tile.set_starting_connections(first, second)
    #     next_entry = map_entry_to_exit[current_tile.exit]
    #     next_column, next_row = current_tile.next
    #     self.mark_right(current_tile, column, row)
    #     current_tile = Tile(self.map[next_row][next_column], next_column, next_row, next_entry)
    #     self.mark_right(current_tile, next_column, next_row)
    #     while current_tile.value != "S":
    #         next_entry = map_entry_to_exit[current_tile.exit]
    #         next_column, next_row = current_tile.next
    #         current_tile = Tile(self.map[next_row][next_column], next_column, next_row, next_entry)
    #         self.mark_right(current_tile, next_column, next_row)
    #     self.flood_fill()

    # def mark_right(self, current_tile, column, row):
    #     map_entry_to_right = {"north": (column - 1, row), "east": (column, row - 1), "south": (column + 1, row),
    #                           "west": (column, row + 1)}
    #     right_hand_one = map_entry_to_right[current_tile.entry]
    #     if self.updated_map[right_hand_one[1]][right_hand_one[0]] == ".":
    #         self.updated_map[right_hand_one[1]][right_hand_one[0]] = "R"
    #         self.rights += 1
    #     if current_tile.value == "L" and current_tile.entry == "north":
    #         if self.updated_map[row][column + 1] == ".":
    #             self.updated_map[row][column + 1] = "R"
    #             self.rights += 1
    #     elif current_tile.value == "7" and current_tile.entry == "south":
    #         if self.updated_map[row][column - 1] == ".":
    #             self.updated_map[row][column - 1] = "R"
    #             self.rights += 1
    #     elif current_tile.value == "F" and current_tile.entry == "east":
    #         if self.updated_map[row - 1][column] == ".":
    #             self.updated_map[row - 1][column] = "R"
    #             self.rights += 1
    #     elif current_tile.value == "J" and current_tile.entry == "west":
    #         if self.updated_map[row + 1][column] == ".":
    #             self.updated_map[row + 1][column] = "R"
    #             self.rights += 1

    # def flood_fill(self):
    #     updates = []
    #     for row, line in enumerate(self.updated_map):
    #         for column, square in enumerate(self.updated_map):
    #             if self.updated_map[row][column] == "R":
    #                 if row > 0:
    #                     if self.updated_map[row - 1][column] == ".":
    #                         updates.append((column, row - 1))
    #                 if row < len(self.map) - 1:
    #                     if self.updated_map[row + 1][column] == ".":
    #                         updates.append((column, row + 1))
    #                 if column > 0:
    #                     if self.updated_map[row][column - 1] == ".":
    #                         updates.append((column - 1, row))
    #                 if column < len(self.map[0]) - 1:
    #                     if self.updated_map[row][column + 1] == ".":
    #                         updates.append((column + 1, row))
    #     if updates:
    #         for update in updates:
    #             self.updated_map[update[1]][update[0]] = "R"
    #             self.rights += 1
    #         self.flood_fill()


    def mark_the_map(self):
        for row, line in enumerate(self.map):
            horizontal = []
            for column, square in enumerate(line):
                if (column, row) in self.path:
                    if self.map[row][column] == "-":
                        horizontal.append("-")
                    elif self.map[row][column] == "|":
                        horizontal.append("|")
                    else:
                        horizontal.append("O")
                else:
                    horizontal.append(".")
            self.updated_map.append(horizontal)

    def mark_interiors(self):
        for row, line in enumerate(self.updated_map):
            new_line = []
            for column, square in enumerate(line):
                if square == ".":
                    if line[column:].count("|") % 2 == 1:
                        new_line.append("R")
                    else:
                        new_line.append(".")
                else:
                    new_line.append(square)
            self.updated_map[row] = new_line

if __name__ == "__main__":
    the_map = TheMap("example4.txt")
    print(f"Furthest point = {the_map.loop_total/2} steps")
    for row in the_map.updated_map:
        print("".join(row))
    print(f"There are {the_map.rights} Rs")