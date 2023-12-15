from StringHash import StringHash

class CommandList:
    def __init__(self, command_data):
        self.command_strings = []
        self.load_data(command_data)
        self.hashed_command_strings = []
        self.hash_commands()
        self.sum_of_results = 0
        self.get_sum_of_results()

    def load_data(self, command_data):
        with open(command_data, "r") as the_file:
            for line in the_file:
                line = line.strip()
                self.command_strings = line.split(",")

    def hash_commands(self):
        for command in self.command_strings:
            self.hashed_command_strings.append(StringHash(command))

    def get_sum_of_results(self):
        for hashed_string in self.hashed_command_strings:
            self.sum_of_results += hashed_string.hashed_value

if __name__ == "__main__":
    command_list = CommandList("input.txt")
    print(command_list.sum_of_results)