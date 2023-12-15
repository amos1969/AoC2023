from StringHash import StringHash
from Box import Box
from Lens import Lens

class CommandList:
    def __init__(self, command_data):
        self.command_strings = []
        self.load_data(command_data)
        self.boxes = []
        for i in range(256):
            self.boxes.append(Box(i))
        self.process_command()
        self.focal_total = 0
        self.calculate_focal_total()

    def process_command(self):
        for command in self.command_strings:
            label = ""
            for index, character in enumerate(command):
                if character == "-":
                    hash_value = StringHash(label).hashed_value
                    self.boxes[hash_value].remove_lens_from_box(Lens(label, 0))
                    break
                elif character == "=":
                    hash_value = StringHash(label).hashed_value
                    lens_value = int(command[index+1:])
                    self.boxes[hash_value].add_lens_to_box(Lens(label, lens_value))
                else:
                    label += character

    def load_data(self, command_data):
        with open(command_data, "r") as the_file:
            for line in the_file:
                line = line.strip()
                self.command_strings = line.split(",")

    def calculate_focal_total(self):
        for box in self.boxes:
            self.focal_total += box.box_total

if __name__ == "__main__":
    command_list = CommandList("input.txt")
    for box in command_list.boxes:
        print(box)
    print(command_list.focal_total)
