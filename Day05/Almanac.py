from MappingGroup import MappingGroup
class Almanac:
    def __init__(self, almanac_data):
        self.data = []
        self.seeds = []
        self.load_data(almanac_data)
        # self.generate_seeds()
        self.lowest_location = None
        self.process_seeds()

    def process_seeds(self):
        for index in range(0, len(self.seeds), 2):
            start = self.seeds[index]
            value_range = self.seeds[index+1]
            for seed in range(start, start + value_range):
                output_value = seed
                # result = f"Seed {output_value} -> "
                for mapping_group in self.data:
                    output_value = mapping_group.get_mapping(output_value)
                    # result += f"{mapping_group.title} - {output_value} -> "
                # print(result)
                if not self.lowest_location:
                    self.lowest_location = output_value
                else:
                    self.lowest_location = min(self.lowest_location, output_value)

    def generate_seeds(self):
        generated_seeds = []
        for index in range(0, len(self.seeds), 2):
            start = self.seeds[index]
            value_range = self.seeds[index+1]
            for seed in range(start, start+value_range):
                generated_seeds.append(seed)
        self.seeds = generated_seeds


    def load_data(self, almanac_data):
        with open(almanac_data, "r") as the_file:
            next_line_title = False
            title = ""
            maps = []
            for line in the_file:
                line = line.strip()
                if "seeds" in line:
                    title, values = line.split(":")
                    values = values.split(" ")
                    for value in values:
                        if value:
                            self.seeds.append(int(value))
                    continue
                else:
                    if not line:
                        next_line_title = True
                        if maps:
                            self.data.append(MappingGroup(title, maps))
                            title = ""
                            maps = []
                    else:
                        if next_line_title:
                            next_line_title = False
                            title = line
                        else:
                            maps.append(line)


if __name__ == "__main__":
    almanac = Almanac("input.txt")
    print(almanac.lowest_location)
