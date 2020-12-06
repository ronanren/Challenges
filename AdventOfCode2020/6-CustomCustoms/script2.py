import sys

lines = []
temp = []
for line in sys.stdin:
    if (line != "\n"):
        temp.append(line.replace("\n", ""))
    else:
        lines.append(temp)
        temp = []
lines.append(temp)

res = 0

for line in lines:
    sets = []
    for i in line:
        sets.append(set(i))
    res += len(set.intersection(*sets))
    
print(res)