import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))
interval = []
i = 0
while lines[i] != "":
    for j in lines[i].split(": ")[1].split(" or "):
        interval.append(range(int(j.split('-')[0]), int(j.split('-')[1]) + 1))
    i += 1
i += 2
ticket = lines[i].split(',')
nearbyTicket = []
for j in range(i+3, len(lines)):
    nearbyTicket.append(lines[j])

def inRange(interval, number):
    res = False
    for i in interval:
        if (number in i):
            res = True
            break
    return res

notValid = []
for i in nearbyTicket:
    for j in i.split(','):
        if (not inRange(interval, int(j))):
            notValid.append(int(j))

print(sum(notValid))