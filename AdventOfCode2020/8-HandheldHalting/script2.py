import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))

def success(lines):
    loop, success = False, False
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
            loop = True
        if i == len(lines):
            loop, success = True, True
    return (success, accumulator)

i = -1
temp = lines
while not success(temp)[0]:
    i += 1
    temp = lines.copy()
    while temp[i].split(" ")[0] == "acc":
        i += 1
    if (temp[i].split(" ")[0] == "jmp"):
        temp[i] = "nop " + temp[i].split(" ")[1]
    else:
        temp[i] = "jmp " + temp[i].split(" ")[1]

print(success(temp)[1])