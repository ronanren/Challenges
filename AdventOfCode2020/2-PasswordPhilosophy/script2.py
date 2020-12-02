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
    if ((password[interval1 - 1] == letter) ^ (password[interval2 - 1] == letter)):
        res += 1

print (res)
