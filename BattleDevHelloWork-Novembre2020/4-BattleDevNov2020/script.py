import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

bytes = lines[1].split(" ")
res = [0] * 256
for operation in lines[2:]:
    result = 0
    for i in range(int(operation.split(' ')[0]), int(operation.split(' ')[1]) + 1):
         result = result ^ int(bytes[i])
    res[result] += 1
        
print(" ".join([str(i) for i in res]))