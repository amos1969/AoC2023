from Part import Part
from Workflow import Workflow

class PileOfParts:
    def __init__(self, parts_pile_data):
        self.parts = []
        self.workflows = dict()
        self.load_data(parts_pile_data)
        self.apply_workflows()
        self.total_score = 0
        self.find_total_score()

    def load_data(self, parts_pile_data):
        gap_reached = False
        with open(parts_pile_data) as the_file:
            for line in the_file:
                line = line.strip()
                if line == "":
                    gap_reached = True
                    continue
                if not gap_reached:
                    workflow = Workflow(line)
                    self.workflows[workflow.label] = workflow
                else:
                    part = Part(line)
                    self.parts.append(part)

    def apply_workflows(self):
        for part in self.parts:
            while not part.accepted and not part.rejected:
                self.workflows[part.next].check_rules(part)
                if part.next == "A":
                    part.accepted = True
                if part.next == "R":
                    part.rejected = True

    def find_total_score(self):
        for part in self.parts:
            if part.accepted:
                self.total_score += part.score

if __name__ == "__main__":
    pile_of_parts = PileOfParts("input.txt")
    print(pile_of_parts.total_score)
