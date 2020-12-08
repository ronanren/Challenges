import sys

lines = []
for line in sys.stdin:
    lines.append(line)

loop = False
accumulator = 0
i = 0
visited = []

while not loop:
    visited.append(i)
    if lines[i].split(" ")[0] == "nop":
        i += 1
    elif lines[i].split(" ")[0] == "acc":
        accumulator = accumulator + int(lines[i].split(" ")[1])
        i += 1
    elif lines[i].split(" ")[0] == "jmp":
        i = i + int(lines[i].split(" ")[1])
    if i in visited:
        print(accumulator)
        loop = True
    

