import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

res = 0
count = 1
last = lines[2]
for number in lines[2:]:
    if (number == last):
        count += 1
    else:
        count = 1
    if (count > res):
        res = count
    last = number

print (res)