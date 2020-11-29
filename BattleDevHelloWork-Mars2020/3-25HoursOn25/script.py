import sys
from datetime import datetime, timedelta

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
slots = [[], [], [], [], []]

for slot in lines[1:]:
    slots[int(slot.split(" ")[0]) - 1].append(slot.split(" ")[1])
day = 0
h = "08:00"
res = ""
while day < 5 and h != "Found":
    h = "08:00" 
    while h != "Found" and h != "Not found":
        hourend = datetime.strptime(h, '%H:%M') + timedelta(minutes = 59)
        test = True
        for slot in slots[day]:
            if (not (int(slot.split('-')[0].replace(":", "")) <= int(h.replace(":", "")) <= int(slot.split('-')[1].replace(":", ""))) and not (int(slot.split('-')[0].replace(":", "")) <= int(hourend.strftime("%H:%M").replace(":", "")) <= int(slot.split('-')[1].replace(":", "")))):
                res = str(day + 1) + " " + str(h) + "-" + str(hourend.strftime("%H:%M"))
            else:
                test = False
        if (test == True):
            h = "Found"

        if (h != "Found" and h.split(":")[1] == "59"):
            h = str("{:02d}".format(int(h.split(":")[0]) + 1)) + ":00"
        elif (h != "Found"):
            h = h.split(":")[0] + ":" + str("{:02d}".format(int(h.split(":")[1]) + 1))
        if (h == "17:00"):
            h = "Not found"
    day += 1

print (res)