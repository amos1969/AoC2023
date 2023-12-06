class Race:
    def __init__(self, time, distance):
        self.time = time
        self.record_distance = distance
        self.attempts = dict()
        self.calculate_attempts()
        self.record_beaten = 0
        self.calculate_victories()

    def calculate_attempts(self):
        for i in range(self.time):
            self.attempts[i] = i * (self.time - i)

    def calculate_victories(self):
        for distance in self.attempts.values():
            if distance > self.record_distance:
                self.record_beaten += 1


if __name__ == "__main__":
    race = Race(30, 200)
    print(race.record_beaten)