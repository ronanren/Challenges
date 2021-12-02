import sys

lines = []
for line in sys.stdin:
	lines.append(int(line.rstrip('\n')))

result = 0
for x in range(1, len(lines)):
    if (lines[x-1] < lines[x]):
        result += 1

print(result)