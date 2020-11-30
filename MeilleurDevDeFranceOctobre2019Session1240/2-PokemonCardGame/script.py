import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

sacha = lines[1].split(" ")
you = lines[2].split(" ")

while sacha != [] and you != []:
    if (int(sacha[0]) > int(you[0])):
        sacha.append(sacha.pop(0))
        you.pop(0)
    elif (int(sacha[0]) < int(you[0])):
        you.append(you.pop(0))
        sacha.pop(0)
    else:
        you.pop(0)
        sacha.pop(0)
    

if (sacha == [] and you == []):
    print("N")
elif (sacha == []):
    print("G")
else:
    print("P")