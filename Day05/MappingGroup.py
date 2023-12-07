from Mapping import Mapping

class MappingGroup:
    def __init__(self, title, mappings):
        self.title = title
        self.mappings = []
        for mapping in mappings:
            self.mappings.append(Mapping(mapping))

    def get_mapping(self, value):
        for mapping in self.mappings:
            if mapping.contains(value):
                return mapping.get_map(value)
        return value

    def __repr__(self):
        lines = f"{self.title} \n"
        for mapping in self.mappings:
            lines += str(mapping)
        return lines

if __name__ == "__main__":
    seed_to_soil = MappingGroup("seed-to-soil", ["50 98 2", "52 50 48"])
    print("79 -> ", seed_to_soil.get_mapping(79))
    print("14 -> ", seed_to_soil.get_mapping(14))
    print("55 -> ", seed_to_soil.get_mapping(55))
    print("13 -> ", seed_to_soil.get_mapping(13))