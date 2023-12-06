
lines = open("data/day6_small", "r").readlines()
times = [int(line) for line in lines[0].split(":")[1].rstrip().split(" ") if line != ""]
distance = [int(line) for line in lines[1].split(":")[1].rstrip().split(" ") if line != ""]
print(times)
print(distance)