import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

horizontal, depth = 0,0
for line in lines:
	command = line.split(" ")[0]
	value = int(line.split(" ")[1])
	if command == "forward":
		horizontal += value
	else:
		if (command == "down"):
			depth += value
		else:
			depth -= value

print(horizontal*depth)