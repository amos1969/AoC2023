from RoundStone import RoundStone

class Dish:
    def __init__(self, dish_data):
        self.loop_size = 1000000000
        self.initial_dish = []
        self.load_data(dish_data)
        self.working_dish = self.initial_dish[:]
        self.loop_found = False
        self.maps = []
        self.loop_start = 0
        self.loop_end = 0
        self.offset = 0
        while not self.loop_found:
            stringified_map = ""
            for row in self.working_dish:
                stringified_map += "".join(row)
            if stringified_map not in self.maps:
                self.maps.append(stringified_map)
            else:
                self.loop_end = len(self.maps) - 1
                self.loop_start = self.maps.index(stringified_map) - 1
                self.loop_found = True
            self.move_balls_north()
            self.move_balls_west()
            self.move_balls_south()
            self.move_balls_east()

        self.offset = (self.loop_size - self.loop_start) % (self.loop_end - self.loop_start)
        for _ in range(self.loop_start - 1 + self.offset):
            self.move_balls_north()
            self.move_balls_west()
            self.move_balls_south()
            self.move_balls_east()

        self.north_total = 0
        self.calculate_north_weight()

    def move_balls_north(self):
        for row, line in enumerate(self.working_dish):
            for column, square in enumerate(line):
                if square == "O":
                    ball = RoundStone(column, row)
                    while ball.can_move:
                        if ball.current_row > 0:
                            if self.working_dish[ball.current_row - 1][column] == ".":
                                ball.current_row -= 1
                                self.working_dish[ball.current_row + 1][column] = "."
                            else:
                                ball.can_move = False
                        else:
                            ball.can_move = False
                        self.working_dish[ball.current_row][column] = "O"

    def move_balls_west(self):
        for row, line in enumerate(self.working_dish):
            temp_line = line[:]
            for column, square in enumerate(temp_line):
                if square == "O":
                    ball = RoundStone(column, row)
                    while ball.can_move:
                        if ball.current_column > 0:
                            if self.working_dish[row][ball.current_column - 1] == ".":
                                ball.current_column -= 1
                                self.working_dish[row][ball.current_column + 1] = "."
                            else:
                                ball.can_move = False
                        else:
                            ball.can_move = False
                        self.working_dish[row][ball.current_column] = "O"

    def move_balls_south(self):
        for row in range(len(self.working_dish) - 1, -1, -1):
            line = self.working_dish[row]
            for column, square in enumerate(line):
                if square == "O":
                    ball = RoundStone(column, row)
                    while ball.can_move:
                        if ball.current_row < len(self.working_dish) - 1:
                            if self.working_dish[ball.current_row + 1][column] == ".":
                                ball.current_row += 1
                                self.working_dish[ball.current_row - 1][column] = "."
                            else:
                                ball.can_move = False
                        else:
                            ball.can_move = False
                        self.working_dish[ball.current_row][column] = "O"
    def move_balls_east(self):
        for row, line in enumerate(self.working_dish):
            temp_line = line[:]
            for column in range(len(temp_line) - 1, -1, -1):
                square = temp_line[column]
                if square == "O":
                    ball = RoundStone(column, row)
                    while ball.can_move:
                        if ball.current_column < len(temp_line) - 1:
                            if self.working_dish[row][ball.current_column + 1] == ".":
                                ball.current_column += 1
                                self.working_dish[row][ball.current_column - 1] = "."
                            else:
                                ball.can_move = False
                        else:
                            ball.can_move = False
                        self.working_dish[row][ball.current_column] = "O"

    def calculate_north_weight(self):
        row_score = len(self.working_dish)
        for row in self.working_dish:
            self.north_total += row.count("O") * row_score
            row_score -= 1


    def load_data(self, dish_data):
        with open(dish_data, "r") as the_file:
            for line in the_file:
                line = line.strip()
                self.initial_dish.append(list(line))

if __name__ == "__main__":
    dish = Dish("example.txt")
    # for row in dish.working_dish:
    #     print("".join(row))
    print(f"Final total: {dish.north_total}")