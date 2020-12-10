import sys

lines = []
for line in sys.stdin:
    lines.append(int(line.replace("\n", "")))
lines.append(max(lines) + 3)

arrangements = []

array = sorted(lines)[:-1]

for i, value in enumerate(array):
    if (i + 1 < len(array) and (array[i+1] - value) < 3 and (array[i+1] - array[i-1]) < 3):
        array.remove(value)

print(array)