import sys
import itertools

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))

timestamp = int(lines[0])
buses = [i for i in lines[1].split(",")]

combi = itertools.permutations([i for i in range(0, 100000)], 2)