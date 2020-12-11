import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))

for i, value in enumerate(lines):
    lines[i] = [i for i in value]

def occupied(lines, i, j):
    seats = 0
    if (i > 0):
        if (lines[i-1][j] == '#'):
            seats += 1
        if (j > 0 and lines[i-1][j-1] == '#'):
            seats += 1
        if (j + 1 < len(lines[i-1]) and lines[i-1][j+1] == '#'):
            seats += 1
    if (i + 1 < len(lines)):
        if (lines[i+1][j] == '#'):
            seats += 1
        if (j > 0 and lines[i+1][j-1] == '#'):
            seats += 1
        if (j + 1 < len(lines[i+1]) and lines[i+1][j+1] == '#'):
            seats += 1
    if (j > 0):
        if (lines[i][j-1] == '#'):
            seats += 1
    if (j + 1 < len(lines[i])):
        if (lines[i][j+1] == '#'):
            seats += 1
    return seats


def makeRound(lines):
    change = 0
    seatLayout = [row[:] for row in lines]
    for i, line in enumerate(lines):
        for j, seat in enumerate(line):
            if (seat == 'L' and occupied(lines, i, j) == 0):
                seatLayout[i][j] = '#'
                change += 1
            elif (seat == '#' and occupied(lines, i, j) >= 4):
                seatLayout[i][j] = 'L'
                change += 1
    return seatLayout, change


state = makeRound(lines)
while state[1] != 0:
    state = makeRound(state[0])

seatsOccupied = 0
for i in state[0]:
    seatsOccupied += i.count("#")

print(seatsOccupied)
