import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

nbr = 0
x = 0

for i in lines:
    if (i[x] == '#'):
        nbr += 1
    if (len(i) <= x + 3):
        x = x + 3 - len(i)
    else:
        x += 3

print (nbr)