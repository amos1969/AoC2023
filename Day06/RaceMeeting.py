from Race import Race

class RaceMeeting:
    def __init__(self, race_data):
        self.get_times_and_distances(race_data)
        self.races = []
        self.generate_races()
        self.record_product = 1
        self.calculate_record_product()

    def get_times_and_distances(self, race_data):
        with open(race_data, "r") as the_file:
            lines = []
            for line in the_file:
                line = line.strip()
                lines.append(line)
        title, timings = lines[0].split(":")
        title, lengths = lines[1].split(":")
        timings = timings.split(" ")
        lengths = lengths.split(" ")
        self.time = ""
        self.distance = ""
        for time in timings:
            if time:
                self.time += time
        for distance in lengths:
            if distance:
                self.distance += distance
        self.time = int(self.time)
        self.distance = int(self.distance)

    def generate_races(self):
        # for i in range(len((self.times))):
        #     self.races.append(Race(self.times[i], self.distances[i]))
        self.races.append(Race(self.time, self.distance))

    def calculate_record_product(self):
        for race in self.races:
            self.record_product *= race.record_beaten

if __name__ == "__main__":
    race_meeting = RaceMeeting("input.txt")
    print(race_meeting.record_product)