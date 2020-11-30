import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
    
res = []

for i in lines[1:]:
    if i == i[::-1]:
        res.append(i)

print (" ".join([str(i) for i in res]))