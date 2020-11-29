import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

res = []
divisible = [2, 3, 5, 7, 11]
for color in lines[1:]:
    for div in divisible:
        if (int(color) % div == 0):
            if div not in res:
                res.append(div)

print(" ".join([str(i) for i in sorted(res)]))