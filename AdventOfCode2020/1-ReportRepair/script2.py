import sys
from itertools import combinations

lines = []
for line in sys.stdin:
	lines.append(int(line.rstrip('\n')))

res = 1

for p in combinations(lines,3):
  if sum(p)==2020:
    for nbr in p:
        res *= nbr

print (res)