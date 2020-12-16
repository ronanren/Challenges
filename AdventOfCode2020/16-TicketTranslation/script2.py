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
for i, row in enumerate(rows):
    j = 0
    for p in range(0, len(interval)):
        if (inRangeRow(interval[j], row) <= 4 and j not in used):
            used.append(j)
            res[lines[i].split(':')[0]] = j
            break
        j += 1
    
result = 1
for i, value in res.items():
    if ("departure" in i):
        result *= int(ticket[value])
        print(str(i) + " " + ticket[value])

print (result)
# 676328537453 too low
