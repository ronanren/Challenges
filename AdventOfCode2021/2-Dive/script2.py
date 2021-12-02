import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

horizontal, depth, aim = 0,0,0
for line in lines:
    command = line.split(" ")[0]
    value = int(line.split(" ")[1])
    if command == "down":
        aim += value
    elif command == "up":
        aim -= value
    else:
        horizontal += value
        depth += aim * value

print(horizontal*depth)