class Hand:
    def __init__(self, cubes):
        self.valid = False
        self.green = 0
        self.red = 0
        self.blue = 0
        self.calculate_values(cubes)
        self.check_validity()

    def calculate_values(self, cubes):
        numbers_and_colours = cubes.split(",")
        for index, cube in enumerate(numbers_and_colours):
            if cube[0] == " ":
                cube = cube.strip()
            deal = cube.split(" ")
            if deal[1] == "green":
                self.green = int(deal[0])
            elif deal[1] == "red":
                self.red = int(deal[0])
            elif deal[1] == "blue":
                self.blue = int(deal[0])

    def check_validity(self):
        self.valid = self.red <= 12 and self.green <= 13 and self.blue <= 14


if __name__ == "__main__":
    hand_1 = Hand("3 green, 1 blue, 15 red")
    hand_2 = Hand(" 1 red, 7 blue, 3 green")