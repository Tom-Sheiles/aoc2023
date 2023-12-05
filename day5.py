# Part 1

lines = [ line for line in open("data/day5_small", "r").readlines() if line != '\n']
seeds = [int(seed) for seed in lines[0].split(":")[1].lstrip().rstrip().split(" ")]


print(seeds)
