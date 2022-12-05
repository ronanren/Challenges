import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

res = []
sum = 0
for calorie in lines:
    if (calorie == ""):
        res.append(sum)
        sum = 0
    else:
        sum += int(calorie)
res.append(sum)

res.sort()
print(res[-1] + res[-2] + res[-3])