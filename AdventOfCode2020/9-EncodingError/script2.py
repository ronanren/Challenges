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


def contiguous(lines):
    i = 0
    contiguous = 2
    invalidNumber = checkProperty(lines, 25, 26)
    found = False
    while not found:
        summ = 0
        for j in range(i, i+contiguous):
            summ += lines[j]
        if (summ == invalidNumber):
            res = lines[i:i+contiguous]
            found = True
        if (i >= len(lines) - contiguous):
            contiguous += 1
            i = 0
        elif (contiguous + 1 < len(lines)):
            i += 1
        else:
            print("not found")
            break
    return res

array = contiguous(lines)
print(max(array) + min(array))