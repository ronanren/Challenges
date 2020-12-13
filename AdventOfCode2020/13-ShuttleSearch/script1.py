import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))

timestamp = int(lines[0])
buses = [int(i) for i in lines[1].split(",") if (i != 'x')]
result = {}

for i in buses:
    depart = i
    j = 1
    while depart < timestamp:
        depart = i * j
        j += 1
    result[i] = depart

minimum = timestamp + 1000
ids = 0
for key, value in result.items():
    if (minimum > value):
        minimum = value
        ids = key

print(ids * (minimum - timestamp))
