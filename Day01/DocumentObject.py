from LineObject import LineObject


class DocumentObject:
    def __init__(self, problem_input):
        self.lines = []
        self.grand_total = 0
        self.get_problem_data(problem_input)
        self.calculate_grand_total()

    def get_problem_data(self, problem_input):
        with open(problem_input, "r") as the_file:
            for line in the_file:
                line = line.strip()
                self.lines.append(LineObject(line))

    def calculate_grand_total(self):
        for line_object in self.lines:
            self.grand_total += line_object.extracted_number
