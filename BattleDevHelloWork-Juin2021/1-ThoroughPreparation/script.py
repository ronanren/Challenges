import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

D = int(lines[0]) # the mass of propellant required for takeoff in kg
L =  int(lines[1]) # the total distance of the trip in astronomical units

print(D + L * 5)