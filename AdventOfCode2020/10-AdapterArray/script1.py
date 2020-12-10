import sys

lines = []
for line in sys.stdin:
    lines.append(int(line.replace("\n", "")))
lines.append(max(lines) + 3)

diff1 = 0
diff3 = 0
outlet = 0

while True:
    if (outlet + 1 in lines):
        diff1 += 1
        outlet += 1
    elif (outlet + 2 in lines):
        outlet += 1
    elif (outlet + 3 in lines):
        diff3 += 1
        outlet += 3
    else:
        break
    

print(str(diff1 * diff3))