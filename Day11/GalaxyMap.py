class GalaxyMap:
    def __init__(self, galaxy_data):
        self.expansion = 999999
        self.initial_galaxy = []
        self.expanded_galaxy = []
        self.coordinates = []
        self.number_of_rows = 0
        self.number_of_columns = 0
        self.load_data(galaxy_data)
        self.expand_galaxy()
        self.total_distances = 0
        self.calculate_distances()

    def load_data(self, galaxy_data):
        with open(galaxy_data, "r") as the_file:
            for line in the_file:
                line = line.strip()
                self.initial_galaxy.append(list(line))
        self.number_of_rows = len(self.initial_galaxy)
        self.number_of_columns = len(self.initial_galaxy[0])

    def expand_galaxy(self):
        initial_coordinates = self.get_coordinates(self.initial_galaxy)
        included_columns = []
        included_rows = []
        for coordinate in initial_coordinates:
            included_columns.append(coordinate[0])
            included_rows.append(coordinate[1])
        included_columns = set(included_columns)
        included_rows = set(included_rows)
        base_columns = set()
        for i in range(self.number_of_columns):
            base_columns.add(i)
        base_rows = set()
        for i in range(self.number_of_rows):
            base_rows.add(i)
        excluded_columns = list(base_columns.difference(included_columns))
        excluded_rows = list(base_rows.difference(included_rows))
        for index, coordinate in enumerate(initial_coordinates):
            column_offset = 0
            for column in excluded_columns:
                if column < coordinate[0]:
                    column_offset += 1
            row_offset = 0
            for row in excluded_rows:
                if row < coordinate[1]:
                    row_offset += 1
            initial_coordinates[index] = (coordinate[0] + column_offset * self.expansion, coordinate[1] + row_offset * self.expansion)
        self.coordinates = initial_coordinates[:]

    def calculate_distances(self):
        galaxy_coordinates = self.coordinates[:]
        count = 0
        while len(galaxy_coordinates):
            horizontal = 0
            vertical = 0
            current_galaxy = galaxy_coordinates.pop(0)
            for galaxy in galaxy_coordinates:
                count += 1
                horizontal += abs(current_galaxy[0] - galaxy[0])
                vertical += abs(current_galaxy[1] - galaxy[1])
            self.total_distances += horizontal + vertical


    def get_coordinates(self, a_galaxy):
        coordinates = set()
        for row, line in enumerate(a_galaxy):
            for column, point in enumerate(line):
                if point != ".":
                    coordinates.add((column, row))
        return list(coordinates)


if __name__ == "__main__":
    galaxy = GalaxyMap("input.txt")
    print(galaxy.total_distances)