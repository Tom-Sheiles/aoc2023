# Part 1
# calulates the sum of the ids of the games that are valid given the total number of cubes in the bag

class Game:
    def __init__(self, gamestr):
        self.gamestr = gamestr.rstrip().replace(";",",").split(":")
        self.id = int(self.gamestr[0].split(" ")[1])
        self.values  = list(map(lambda str: str.lstrip().split(" "), self.gamestr[1].split(",")))

        # blue/red/green are parsed as three sperate lists of the interger values of each color for each game
        self.blue = (list(map(lambda cube: int(cube[0]), list(filter(lambda cube: cube[1] == "blue",self.values)))))
        self.red = (list(map(lambda cube: int(cube[0]), list(filter(lambda cube: cube[1] == "red",self.values)))))
        self.green = (list(map(lambda cube: int(cube[0]), list(filter(lambda cube: cube[1] == "green",self.values)))))

        # find the minimum number of each color needed for the game to be valid
        self.min_blue = max(self.blue)
        self.min_red = max(self.red)
        self.min_green = max(self.green)
        return

    # Game is considered valid if all the values of cubes in each list are lower than the specified value
    def is_valid(self, discriminator):
        valid_blue = all(i <= discriminator["blue"] for i in self.blue)
        valid_red = all(i <= discriminator["red"] for i in self.red)
        valid_green = all(i <= discriminator["green"] for i in self.green)
        return valid_blue and valid_green and valid_red


# Construct list of games from input file
games = list(map(lambda str: Game(str), open("data/day2", "r")))

# find the sublist of games for which the number of cubes of any given color are below the maximum value
valid_games = list(filter(lambda game: game.is_valid({"red":12, "green":13, "blue":14}), games))

# print the sum of the ids of all valid games
print(sum(game.id for game in valid_games))

# part 2
# calculate the sum of the "power" of the minimum number of cubes needed for all the games to be valid
print(sum(list(map(lambda game: game.min_blue * game.min_red * game.min_green,games))))