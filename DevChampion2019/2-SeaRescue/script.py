import sys, math

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

res = 0

for boat in lines[1:]:
    res += math.ceil(int(boat)/10)

print (int(res))