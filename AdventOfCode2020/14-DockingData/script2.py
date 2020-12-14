import sys
from itertools import *

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))

def applyMask(mask, integer):
    res = list("0" * 36)
    binary = "{0:036b}".format(integer)
    for i, val in enumerate(res):
        if (mask[i] == '1' or (binary[i] == '1' and mask[i] != 'X')):
            res[i] = '1'
        elif (mask[i] == '0'):
            res[i] = '0'
        else:
            res[i] = 'X'
    return "".join([i for i in res])

mem = {}
currentMask = ""
for i in lines:
    if (i[0:4] == "mask"):
        currentMask = i.split("= ")[1]
    else:
        combinations = applyMask(currentMask, int(i[i.index("[")+1:i.index("]")]))
        pp = list(product([0,1], repeat=combinations.count('X')))
        for p in pp:
            temp = combinations
            for j in range(0, combinations.count('X')):
                temp = temp.replace('X', str(p[j]), 1)
            mem[str(int(temp, 2))] = i.split("= ")[1]

res = 0
for i in mem.values():
    res += int(i)

print(res)