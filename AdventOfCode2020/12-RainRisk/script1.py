import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))

facing = 'E'
faces = ['N', 'E', 'S', 'W']
values = {'N': 0, 'S': 0, 'E': 0, 'W': 0}

for i in lines:
    if (i[0] == 'F'):
        values[facing] = values[facing] + int(i[1:]) - values[faces[(faces.index(facing) + 2) % 4]]
        values[faces[(faces.index(facing) + 2) % 4]] = 0
    if (i[0] in ['N', 'S', 'E', 'W']):
        values[i[0]] += int(i[1:])
    if (i[0] == 'L'):
        facing = faces[(faces.index(facing) - int(int(i[1:])/90)) % 4]
    if (i[0] == 'R'):
        facing = faces[int(int(i[1:])/90 + faces.index(facing)) % 4]

print(abs(values['E'] - values['W']) + abs(values['N'] - values['S']))