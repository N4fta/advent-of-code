import re

fs = open("2023/day2/input.txt")

def part1():
    red_max = 12
    green_max = 13
    blue_max = 14


    sum_gameIDs = 0
    for line in iter(fs.readline, ''): # Iterate this function until it returns '', super neat stuff
        splits = line.split(':', 1)
        gameID = splits[0].split(' ', 1)[1]
        sets = splits[1]

        reds = re.findall("[0-9]+(?= red)", sets)
        greens = re.findall("[0-9]+(?= green)", sets)
        blues = re.findall("[0-9]+(?= blue)", sets)
        possible = True
        possible = all([(possible and int(x) <= 12) for x in reds])
        possible = all([(possible and int(x) <= 13) for x in greens])
        possible = all([(possible and int(x) <= 14) for x in blues])

        # I'm pretty new to python but this feels very pythonic XD

        if possible: sum_gameIDs += int(gameID)

    print(sum_gameIDs)

def part2():
    red_max = 0
    green_max = 0
    blue_max = 0

    sum_powers = 0

    for line in iter(fs.readline, ''):
        splits = line.split(':', 1)
        gameID = splits[0].split(' ', 1)[1]
        sets = splits[1]

        reds = re.findall("[0-9]+(?= red)", sets)
        greens = re.findall("[0-9]+(?= green)", sets)
        blues = re.findall("[0-9]+(?= blue)", sets)

        red_max = max([int(nbr) for nbr in reds])
        green_max = max([int(nbr) for nbr in greens])
        blue_max = max([int(nbr) for nbr in blues]) # I really love LINQ

        power = red_max * green_max * blue_max
        sum_powers += power

    print(sum_powers)

part2()