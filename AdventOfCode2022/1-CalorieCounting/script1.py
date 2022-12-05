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

print(max(res))