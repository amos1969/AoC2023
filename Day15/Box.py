from Lens import Lens
class Box:
    def __init__(self, box_no):
        self.box_no = box_no
        self.slots = []
        self.box_total = 0
        self.update_box_total()

    def remove_lens_from_box(self, lens):
        lens_to_remove = False
        lens_index = None
        for index, existing_lens in enumerate(self.slots):
            if existing_lens.label == lens.label:
                lens_to_remove = True
                lens_index = index
                break
        if lens_to_remove:
            self.slots.pop(lens_index)
        self.update_box_total()

    def add_lens_to_box(self, lens):
        if self.lens_in_box(lens):
            for index, existing_lens in enumerate(self.slots):
                if existing_lens.label == lens.label:
                    self.slots[index] = lens
        else:
            self.slots.append(lens)
        self.update_box_total()

    def lens_in_box(self, new_lens):
        for lens in self.slots:
            if new_lens.label == lens.label:
                return True
        return False

    def update_box_total(self):
        self.box_total = 0
        for index, lens in enumerate(self.slots):
            lens_total = (self.box_no + 1) * (index + 1) * lens.focal_length
            self.box_total += lens_total

    def __repr__(self):
        representation = f"Box {self.box_no}: "
        for lens in self.slots:
            representation += f"[{lens.label} {lens.focal_length}] "
        representation += f"Total: {self.box_total}"
        return representation

if __name__ == "__main__":
    lens_1 = Lens("rn", 1)
    lens_2 = Lens("qp", 4)
    lens_3 = Lens("rn", 2)
    lens_4 = Lens("tt", 5)
    box = Box(0)
    box.add_lens_to_box(lens_1)
    print(box)
    box.add_lens_to_box(lens_2)
    print(box)
    box.remove_lens_from_box(lens_1)
    print(box)
    box.add_lens_to_box(lens_1)
    print(box)
    box.add_lens_to_box(lens_3)
    print(box)
    box.remove_lens_from_box(lens_4)
    print(box)
