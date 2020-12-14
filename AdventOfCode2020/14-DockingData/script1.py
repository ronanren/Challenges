import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))

def applyMask(mask, integer):
    res = list("0" * 36)
    binary = "{0:036b}".format(integer)
    for i, val in enumerate(res):
        if (mask[i] == 'X'):
            res[i] = binary[i]
        elif (mask[i] == '0'):
            res[i] = '0'
        else:
            res[i] = '1'
    return int("".join([i for i in res]), 2)

mem = {}
currentMask = ""
for i in lines:
    if (i[0:4] == "mask"):
        currentMask = i.split("= ")[1]
    else:
        mem[str(i[i.index("[")+1:i.index("]")])] = applyMask(currentMask, int(i.split("= ")[1]))

res = 0
for i in mem.values():
    res += int(i)

print(res)