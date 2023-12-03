# Part 1
# prints the sum of the numbers created by concatinating the first and last digit of each line in the file data/day1
print(sum(map(lambda z: int(z),list(map(lambda y: ''.join([y[i] for i in (0,-1)]),list(map(lambda line: list(filter(lambda chars: not chars.isalpha(), line.rstrip())),open("data/day1", "r"))))))))

# Part 2
# modiification to the first part which also parses numbers spelled out 
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ndict = { "zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9" }

# recursive find function that returns a substring if it exists in the list variable
def findinlist(str, list):
    if len(list) <= 0:
        return -1

    idx = str.find(list[0])
    if idx < 0:
        return findinlist(str, list[1:])
    else:
        return str[idx:idx+len(list[0])]

# recursivly build string attempting to find the first occurance of a number
def consume(str, rest):

    if len(rest) <= 0:
        if not str[-1].isalpha():
            return str[-1]
        else: 
            return str

    parsed_num = findinlist(str, numbers)
    if parsed_num != -1:
        return consume(parsed_num, [])

    if not str[-1].isalpha():
        return consume(str[-1],[])
    else:
        return consume(str + rest[0], rest[1:])


# recursivly build string attempting to find the last occurance of a number
def consume_reverse(str, rest):
    if len(rest) <= 0:
        if not str[0].isalpha():
            return str[0]
        else:
            return str
    
    parsed_num = findinlist(str, numbers)
    if parsed_num != -1:
        return consume_reverse(parsed_num, [])
    
    if not str[0].isalpha():
        return consume_reverse(str[0],[])
    else:
        return consume_reverse(rest[-1] + str, rest[0:-1])

# return a list of the first number in each string
def first_number(x):
    chars = list(x)
    return consume(chars[0], chars[1:])

# return a list of the last number in each string
def last_numbers(x):
    chars = list(x)
    return consume_reverse(chars[-1], chars[0:-1])


# read all lines of the input and construct two lists of the first and last numbers in each
lines = list(map(lambda line: line.rstrip(),open("data/day1", "r")))
first_numbers = list(map(first_number, lines))
last_numbers = list(map(last_numbers, lines))

# convert all spelled out numbers in to digits
first_digits = list(map(lambda y: ndict[y] if y in ndict else y,first_numbers))
last_digits = list(map(lambda y: ndict[y] if y in ndict else y,last_numbers))

# concatinate the two lists into a single list of two digit numbers and print the sum of all of them
concatinated_numbers = list(map(lambda first, last: first+last, first_digits,last_digits))
print(sum(list(map(lambda number: int(number), concatinated_numbers))))