class Card:
    def __init__(self, line):
        self.line = line
        self.winning = [int(n) for n in list(filter(lambda number: number != '', line.split("|")[0].split(":")[1].lstrip().split(" ")))]
        self.played = [int(n) for n in list(filter(lambda number: number != '', line.split("|")[1].lstrip().split(" ")))]

        self.matching = [number for number in self.played if number in self.winning]
        return

    def _recurse_points(self, points, match):
        if len(match) <= 0:
            return points
        return self._recurse_points(points * 2 if points > 0 else 1, match[1:])
    
    def get_points(self):
        return self._recurse_points(0, self.matching)

lines = open("data/day4", "r").readlines()
cards = list(map(lambda line: Card(line.rstrip()), lines))

print(sum([ points.get_points() for points in cards]))