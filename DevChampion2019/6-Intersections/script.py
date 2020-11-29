import sys

input = []
for line in sys.stdin:
	input.append(line.rstrip('\n'))

nbrLines = input[0].split(" ")[0]
nbrStations = input[0].split(" ")[1]
startStation = input[1].split(" ")[0]
destination = input[1].split(" ")[1]

lines = []
for line in input[3:]:
    lines.append(line.split(" "))

for i in range(0, len(lines)):
    if startStation in lines[i]:
        startStationLine = i
for i in range(0, len(lines)):
    if destination in lines[i]:
        destinationLine = i

print ("TODO")