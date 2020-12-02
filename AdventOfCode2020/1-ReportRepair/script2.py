import sys
from itertools import combinations

lines = []
for line in sys.stdin:
	lines.append(int(line.rstrip('\n')))

print({p[0] * p[1] * p[2] for p in combinations(lines, 3) if (sum(p) == 2020)})