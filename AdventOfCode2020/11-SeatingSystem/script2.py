import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))

for i, value in enumerate(lines):
    lines[i] = [i for i in value]

def occupied(lines, i, j):
    seats = 0
    for k in range(i, 0, -1):
        if (lines[k][j] == 'L'):
            break
        if (lines[k][j] == '#'):
            seats += 1
            break
    for k in range(i+1, len(lines)):
        if (lines[k][j] == 'L'):
            break
        if (lines[k][j] == '#'):
            seats += 1
            break
    for k in range(j, 0, -1):
        if (lines[i][k] == 'L'):
            break
        if (lines[i][k] == '#'):
            seats += 1
            break
    for k in range(j+1, len(lines[i])):
        if (lines[i][k] == 'L'):
            break
        if (lines[i][k] == '#'):
            seats += 1
            break
    k = 1
    while i-k >= 0 and j-k >= 0 and lines[i-k][j-k] != "L":
        if (lines[i-k][j-k] == '#'):
            seats += 1
            break
        k += 1  
    k = 1 
    while i-k >= 0 and j+k < len(lines[0]) and lines[i-k][j+k] != "L":
        if (lines[i-k][j+k] == '#'):
            seats += 1
            break
        k += 1 
    k = 1
    while i+k < len(lines) and j+k < len(lines[0]) and lines[i+k][j+k] != "L":
        if (lines[i+k][j+k] == '#'):
            seats += 1
            break
        k += 1 
    k = 1
    while i+k < len(lines) and j-k >= 0 and lines[i+k][j-k] != "L":
        if (lines[i+k][j-k] == '#'):
            seats += 1
            break
        k += 1
    return seats

def makeRound(lines):
    change = 0
    seatLayout = [row[:] for row in lines]
    for i, line in enumerate(lines):
        for j, seat in enumerate(line):
            if (seat == 'L' and occupied(lines, i, j) == 0):
                seatLayout[i][j] = '#'
                change += 1
            elif (seat == '#' and occupied(lines, i, j) >= 5):
                seatLayout[i][j] = 'L'
                change += 1
    return seatLayout, change


state = makeRound(lines)
state = makeRound(state[0])
state = makeRound(state[0])

seatsOccupied = 0
for i in state[0]:
    seatsOccupied += i.count("#")

print(seatsOccupied)

for i in state[0]:
    print("".join([k for k in i]))

# 7378 to high