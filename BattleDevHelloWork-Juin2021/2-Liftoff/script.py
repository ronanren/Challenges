import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

lines = lines[1:]
for button in lines:
	if lines.count(button) == 2:
		print(button)
		break