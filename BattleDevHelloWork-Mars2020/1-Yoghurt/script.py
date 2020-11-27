import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
tab = {}

for color in lines[1:]:
    if (tab.get(color, False)):
        tab[color] += 1
    else:
        tab[color] = 1

for color, nbr in tab.items():
    if (nbr == sorted(tab.values())[-1]):
        res1 = color
    if (nbr == sorted(tab.values())[-2]):
        res2 = color

print (res1 + " " + res2)