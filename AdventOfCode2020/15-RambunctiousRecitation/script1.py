import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))

number = [int(i) for i in lines[0].split(',')]
starting = len(number)

def getLast(number, nbr):
    last = -1
    lastlast = -1
    for i, value in enumerate(number):
        if (value == nbr and number[i:].count(nbr) == 1):
            last = i + 1
        elif (value == nbr and number[i:].count(nbr) == 2):
            lastlast = i + 1
        if (last != -1 and lastlast != -1):
            break
    return last, lastlast

for i in range(0, 2020 - starting):
    if (number[-1] in number[starting:] and number.count(number[-1]) > 1):
        lasts = getLast(number, number[-1])
        number.append(lasts[0] - lasts[1])
    elif (number[-1] not in number[starting:] or number.count(number[-1]) == 1):
        number.append(0)
    

print(number[-1])
