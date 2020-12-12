import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))

facing = 'E'
faces = ['N', 'E', 'S', 'W']
values = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
waypoint = {'N': 1, 'S': 0, 'E': 10, 'W': 0}

for i in lines:
    if (i[0] == 'F'):
        if (waypoint['S'] * int(i[1:]) - values['N'] > 0):
            values['S'] += waypoint['S'] * int(i[1:]) - values['N']
            values['N'] = 0
        else:
            values['N'] = values['N'] - (waypoint['S'] * int(i[1:]))

        if (waypoint['N'] * int(i[1:]) - values['S'] > 0):
            values['N'] += waypoint['N'] * int(i[1:]) - values['S']
            values['S'] = 0
        else:
            values['S'] = values['S'] - (waypoint['N'] * int(i[1:])) 

        if (waypoint['E'] * int(i[1:]) - values['W'] > 0):
            values['E'] += waypoint['E'] * int(i[1:]) - values['W']
            values['W'] = 0
        else:
            values['W'] = values['W'] - (waypoint['E'] * int(i[1:])) 

        if (waypoint['W'] * int(i[1:]) - values['E'] > 0):
            values['W'] += waypoint['W'] * int(i[1:]) - values['E']
            values['E'] = 0
        else:
            values['E'] = values['E'] - (waypoint['W'] * int(i[1:]))
        
    if (i[0] in ['N', 'S', 'E', 'W']):
        waypoint[i[0]] += int(i[1:])
    if (i[0] == 'L'):
        facing = faces[int(int(i[1:])/90 + faces.index(facing)) % 4]
        tempNorth = waypoint['N']
        tempSouth = waypoint['S']
        tempEast = waypoint['E']
        tempWest = waypoint['W']
        waypoint[faces[int(int(i[1:])/90 - faces.index('N')) % 4]] = tempNorth
        waypoint[faces[int(int(i[1:])/90 - faces.index('S')) % 4]] = tempSouth
        waypoint[faces[int(int(i[1:])/90 - faces.index('E')) % 4]] = tempEast
        waypoint[faces[int(int(i[1:])/90 - faces.index('W')) % 4]] = tempWest
    if (i[0] == 'R'):
        facing = faces[int(int(i[1:])/90 - faces.index(facing)) % 4]
        tempNorth = waypoint['N']
        tempSouth = waypoint['S']
        tempEast = waypoint['E']
        tempWest = waypoint['W']
        waypoint[faces[int(int(i[1:])/90 + faces.index('N')) % 4]] = tempNorth
        waypoint[faces[int(int(i[1:])/90 + faces.index('S')) % 4]] = tempSouth
        waypoint[faces[int(int(i[1:])/90 + faces.index('E')) % 4]] = tempEast
        waypoint[faces[int(int(i[1:])/90 + faces.index('W')) % 4]] = tempWest

    

print(abs(values['E'] - values['W']) + abs(values['N'] - values['S']))

# 30940 too high
# 8212 too low 
# Works with example