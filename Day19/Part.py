class Part:
    def __init__(self, scores):
        scores = scores[1:-1]
        split_scores = scores.split(",")
        score = split_scores[0]
        self.x = int(score[2:])
        score = split_scores[1]
        self.m = int(score[2:])
        score = split_scores[2]
        self.a = int(score[2:])
        score = split_scores[3]
        self.s = int(score[2:])
        self.next = "in"

        self.accepted = False
        self.rejected = False
        self.score = self.x + self.m + self.a + self.s

    def __repr__(self):
        return f"X = {self.x}, M = {self.m}, A = {self.a}, S = {self.s} = {self.score} \n"

if __name__ == "__main__":
    part = Part("{x=787,m=2655,a=1222,s=2876}")
    print(f"X: {part.x}")
    print(f"M: {part.m}")
    print(f"A: {part.a}")
    print(f"S: {part.s}")