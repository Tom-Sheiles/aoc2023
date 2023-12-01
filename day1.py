# prints the sum of the numbers created by concatinating the first and last digit of each line in the file data/day1
print(sum(map(lambda z: int(z),list(map(lambda y: ''.join([y[i] for i in (0,-1)]),list(map(lambda line: list(filter(lambda chars: not chars.isalpha(), line.rstrip())),open("data/day1", "r").readlines())))))))
