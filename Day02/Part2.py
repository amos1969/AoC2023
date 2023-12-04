from Game import Game

class Part2:
    def __init__(self, game_input):
        games = []
        with open(game_input, "r") as the_file:
            for line in the_file:
                line = line.strip()
                games.append(Game(line))
        sum_of_powers = 0
        for game in games:
            sum_of_powers += game.power_of_cubes
        print(f"Sum of possible games: {sum_of_powers}")


if __name__ == "__main__":
    # game_examples = Part2("example.txt")
    actual_games = Part2("input.txt")