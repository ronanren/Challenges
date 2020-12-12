import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))

for i, value in enumerate(lines):
    lines[i] = [i for i in value]

def left(lines, i, j):
    res = False
    for k in range(j-1, -1, -1):
        if (lines[i][k] == 'L'):
            break
        elif (lines[i][k] == '#'):
            res = True
            break
    return res

def right(lines, i, j):
    res = False
    for k in range(j+1, len(lines[i])):
        if (lines[i][k] == 'L'):
            break
        elif (lines[i][k] == '#'):
            res = True
            break
    return res

def top(lines, i, j):
    res = False
    for k in range(i-1, -1, -1):
        if (lines[k][j] == 'L'):
            break
        elif (lines[k][j] == '#'):
            res = True
            break
    return res

def bottom(lines, i, j):
    res = False
    for k in range(i+1, len(lines)):
        if (lines[k][j] == 'L'):
            break
        elif (lines[k][j] == '#'):
            res = True
            break
    return res

def leftTop(lines, i, j):
    res = False
    k = 1
    while i-k >= 0 and j-k >= 0:
        if (lines[i-k][j-k] == 'L'):
            break
        elif (lines[i-k][j-k] == '#'):
            res = True
            break
        k += 1
    return res

def rightTop(lines, i, j):
    res = False
    k = 1
    while i-k >= 0 and j+k <= len(lines[i]) - 1:
        if (lines[i-k][j+k] == 'L'):
            break
        elif (lines[i-k][j+k] == '#'):
            res = True
            break
        k += 1     
    return res

def leftBottom(lines, i, j):
    res = False
    k = 1
    while i+k <= len(lines) - 1 and j-k >= 0:
        if (lines[i+k][j-k] == 'L'):
            break
        elif (lines[i+k][j-k] == '#'):
            res = True
            break
        k += 1     
    return res

def rightBottom(lines, i, j):
    res = False
    k = 1
    while i+k < len(lines) and j+k <= len(lines[i]) - 1:
        if (lines[i+k][j+k] == 'L'):
            break
        elif (lines[i+k][j+k] == '#'):
            res = True
            break
        k += 1     
    return res

def occupied(lines, i, j):
    seats = 0
    if (left(lines, i, j)):
        seats += 1
    if (right(lines, i, j)):
        seats += 1
    if (top(lines, i, j)):
        seats += 1
    if (bottom(lines, i, j)):
        seats += 1
    if (leftTop(lines, i, j)):
        seats += 1
    if (rightTop(lines, i, j)):
        seats += 1
    if (leftBottom(lines, i, j)):
        seats += 1
    if (rightBottom(lines, i, j)):
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
            elif (seat == '#' and occupied(lines, i, j) >= 5):
                seatLayout[i][j] = 'L'
                change += 1
    return seatLayout, change


state = makeRound(lines)
while state[1] != 0:
    state = makeRound(state[0])

seatsOccupied = 0

for i in state[0]:
    seatsOccupied += i.count("#")

print("Seats occupied : " + str(seatsOccupied))