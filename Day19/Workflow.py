from Rule import Rule
class Workflow:
    def __init__(self, workflow):
        self.label, self.raw_rules = workflow.split("{")
        self.raw_rules = self.raw_rules[:-1]
        self.rules = []
        self.default = ""
        self.create_rules()

    def create_rules(self):
        split_rules = self.raw_rules.split(",")
        self.default = split_rules.pop(-1)
        for rule in split_rules:
            self.rules.append(Rule(rule))

    def check_rules(self, part):
        for rule in self.rules:
            criteria = rule.check_rule(part)
            if criteria[0]:
                part.next = criteria[1]
                break
        else:
            part.next = self.default

    def __repr__(self):
        return f"Label: {self.label} \n Rules: {self.rules} \n Default: {self.default}"

if __name__ == "__main__":
    workflow = Workflow("px{a<2006:qkq,m>2090:A,rfg}")
    print(workflow.rules)