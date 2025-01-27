import re

fs = open("2023/day3/input.txt")

def findNumbers(prevLine, nextLine, index):
    sum = 0
    numberIndex = 0
    for line in [prevLine, nextLine]:
        number = re.match("\d{1,3}$",line[index-4:index]).string
        if number:
            sum += number
        number = re.match("\d{1,3}$",line[index:index+4])
        if number: 
            sum += number

    return sum



def part1():
    
    sum_partNumbers = 0
    prev_line = ''
    current_line = ''
    next_line = ''
    
    for line in iter(fs.readline, ''): # Iterate this function until it returns '', super neat stuff
        next_line = line

        # Current Line numbers
        digits = re.findall("""\\d{1,3}(?=[^\\.\\d\\n])|(?<=[^\\.\\d\\n])\\d{1,3}""", current_line)
        for x in digits: sum_partNumbers += int(x)

        # Surrounding lines 
        if prev_line == '':
            prev_line = current_line
            current_line = next_line
            continue
        symbols = re.findall("[^\.\d\\n]", line)
        index_symbol = 0
        for symbol in symbols:
            index_symbol = line.find(symbol, index_symbol)
            sum_partNumbers += findNumbers(prev_line, next_line, index_symbol)
        

        prev_line = current_line
        current_line = next_line

    # Last line check


    print(sum_partNumbers)


part1()