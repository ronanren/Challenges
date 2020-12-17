import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))
interval = []
i = 0
while lines[i] != "":
    temp = []
    for j in lines[i].split(": ")[1].split(" or "):
        temp.append(range(int(j.split('-')[0]), int(j.split('-')[1]) + 1))
    interval.append(temp)
    i += 1
i += 2
ticket = lines[i].split(',')
nearbyTicket = []
rows = [[] for i in range(len(ticket))]
for j in range(i+3, len(lines)):
    nearbyTicket.append(lines[j].split(','))
for i in range(i+3, len(lines)):
    for j in range(0, len(lines[i].split(','))):
        rows[j].append(lines[i].split(',')[j])
        
def inRange(interval, number):
    res = False
    for i in interval:
        if (number in i):
            res = True
            break
    return res

def inRangeRow(interval, row):
    nbr = 0
    for i in row:
        if (not inRange(interval, int(i))):
            nbr += 1
    return nbr

res = {}
used = []
for i, inter in enumerate(interval):
    verif = []
    for j, row in enumerate(rows):
        verif.append(inRangeRow(inter, row))
    print(verif)
    
# 676328537453 too low
# not 913983120487
# not 889800648029
