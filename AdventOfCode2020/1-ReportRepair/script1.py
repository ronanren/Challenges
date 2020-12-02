import sys

lines = []
for line in sys.stdin:
	lines.append(int(line.rstrip('\n')))

print({i * (2020 - i) for i in lines if ((2020 - i) in lines)})