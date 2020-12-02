import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

res = 0

for line in lines:
    password = line.split(":")[1].strip()
    letter  = line.split(":")[0].split(" ")[1]
    interval1  = int(line.split(":")[0].split(" ")[0].split("-")[0])
    interval2  = int(line.split(":")[0].split(" ")[0].split("-")[1])
    if (interval1 <= password.count(letter) <= interval2):
        res += 1

print (res)