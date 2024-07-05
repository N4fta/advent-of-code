
fs = open ("2023\day1\input.txt")

totalSum = 0

line: str
for line in iter(fs.readline, ''):
    first, last = '', ''
    for char in line:
        if char.isnumeric ():
            if first == "": first = char
            last = char

    #print(first, last)
    totalSum += int(first+last)
print(totalSum)