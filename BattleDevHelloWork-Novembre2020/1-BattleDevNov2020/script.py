import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
res = 0
for account in lines[1:]:
    if (account[-5:].isdigit()):
        res += 1

print (res)
    