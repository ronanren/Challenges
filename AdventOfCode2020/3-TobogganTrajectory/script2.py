import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))


def nbrTree(right, down, lines):
    nbr = 0
    x = 0
    for i in range(0, len(lines), down):
        if (lines[i][x] == '#'):
            nbr += 1
        if (len(lines[i]) <= x + right):
            x = x + right - len(lines[i])
        else:
            x += right
    return nbr

print (nbrTree(1, 1, lines) * nbrTree(3, 1, lines) * nbrTree(5, 1, lines) * nbrTree(7, 1, lines) * nbrTree(1, 2, lines))