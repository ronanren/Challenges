import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

res = 0
for i in lines[1].split(" "):
    if (int(i) >= 5 and int(i) <= 9):
        res += 1

print (res)