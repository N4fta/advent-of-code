import re

def parsePossibleInt(possibleInt) -> str:
    try:
        return str(int(possibleInt))
    except:
        match possibleInt:
            case "one": return '1'
            case "two": return '2'
            case "three": return '3'
            case "four": return '4'
            case "five": return '5'
            case "six": return '6'
            case "seven": return '7'
            case "eight": return '8'
            case "nine": return '9'
        exit()

def part2():
        # There was a big problem with simply using find all where matches like `eight` in `eightwo` made the regex skip over the `t` in `two`
    # At first I couldn't find this through debugging so I went through the reddit and found someone mention problems with .findall() and not wanting to use look ahead.
    # I went through my code and sure enough that was teh problem

    # They choose to iterate through each digit. But since I saw that solution I I decided to look deeper into regex, what look ahead was and use it
    # To be honest my code is rather inefficient since the pattern is quite long and I iterate twice through every line, but it works! 

    fs = open ("2023/day1/input.txt")

    totalSum = 0
    number_strings = ["one","two","three","four","five","six","seven","eight","nine"]
    regex_first = '|'.join(number_strings)+"|[1-9]"
    regex_last = ''
    # Could have been coded in the list from the start but I thought it might be a fun little challenge
    for i in range(0, len(number_strings)):
        regex_last += number_strings[i][0:-1] + f'(?!{'|'.join(number_strings)})' + number_strings[i][-1] + '|'
    regex_last += "[1-9]"

    line_nbr = 1
    line: str
    for line in iter(fs.readline, ''):
        first_number = re.search(regex_first, line)
        last_number = re.findall(regex_last, line)


        first = parsePossibleInt(first_number.group())
        last = parsePossibleInt(last_number[-1])
        two_digit_number = first + last
        print( f"{line_nbr} - " + two_digit_number)

        line_nbr +=1
        totalSum += int(two_digit_number)
    print(totalSum)


def part2_improved():

    # This second attempt was inspired by the fact that my first function was messy and looked inefficient
    # I don't know if this is more efficient/faster since I have to reverse two strings per line but the pattern is shorter and I assume .search() is faster than .findall() since it stops after the first match
    # Either way this code looks much cleaner

    fs = open ("2023/day1/input.txt")

    totalSum = 0
    number_strings = ["one","two","three","four","five","six","seven","eight","nine"]
    regex_first = '|'.join(number_strings)+"|[1-9]"
    reverse_strings = [x[::-1] for x in number_strings]
    regex_last = '|'.join(reverse_strings)+"|[1-9]"

    for line in iter(fs.readline, ''):
        first_number = re.search(regex_first, line)
        last_number = re.search(regex_last, line[::-1])


        first = parsePossibleInt(first_number.group())
        last = parsePossibleInt(last_number.group()[::-1])
        two_digit_number = first + last
        #print(two_digit_number)

        totalSum += int(two_digit_number)
    print(totalSum)


# Abstracted for testing
part2_improved()