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
    temp = ""
    for i in line:
        temp += i
    res += len(set(temp))

print(res)