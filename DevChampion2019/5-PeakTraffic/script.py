import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

tab = [0] * 86400000

for p in lines[1:]:
	for i in range(int(p.split(" ")[0]), int(p.split(" ")[1])):
		tab[i] += 1

print (max(tab))