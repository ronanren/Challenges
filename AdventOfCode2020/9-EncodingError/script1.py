import sys
from itertools import combinations

lines = []
for line in sys.stdin:
    lines.append(int(line.replace("\n", "")))

def checkProperty(lines, preamble, i):
    verif = False
    for j in combinations(lines[i-25:i], 2):
        if (j[0] + j[1] == lines[i]):
            verif = True
    if (verif):
        return checkProperty(lines, preamble, i+1)
    else:
        return lines[i]


print(checkProperty(lines, 25, 26))