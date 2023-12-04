from Game import Game

class Part1:
    def __init__(self, game_input):
        games = []
        with open(game_input, "r") as the_file:
            for line in the_file:
                line = line.strip()
                games.append(Game(line))
        sum_of_possible_games = 0
        for game in games:
            if game.possible:
                sum_of_possible_games += game.number
        print(f"Sum of possible games: {sum_of_possible_games}")


if __name__ == "__main__":
    # game_examples = Part1("example.txt")
    actual_games = Part1("input.txt")