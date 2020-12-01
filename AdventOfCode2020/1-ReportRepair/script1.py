import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

res = 0

for i in lines:
    for j in lines:
        if (int(i) + int(j) == 2020):
            res = int(i) * int(j)
            break
    if (res != 0):
        break

print (res)