import re

fs = open("2023/day2/input.txt")
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