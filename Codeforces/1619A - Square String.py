import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

for line in lines[1:]:
    if (len(line) % 2 == 0 and line[0:round(len(line)/2)] == line[round(len(line)/2):]):
        print("YES")
    else:
        print("NO")