import sys

lines = []
for line in sys.stdin:
	lines.append(int(line.rstrip('\n')))

result = 0
for x in range(3, len(lines)):
    sum1 = lines[x-3] + lines[x-2] + lines[x-1]
    sum2 = lines[x-2] + lines[x-1] + lines[x]
    if (sum1 < sum2):
        result += 1

print(result)