import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

n = int(lines[0])
res = ""
i = 0
while len(res) != len(lines[1]):
	res += lines[1][i]
	if (i + n >= len(lines[1])):
		i = i + n - len(lines[1]) + 1
	else:
		i += n

print (res)