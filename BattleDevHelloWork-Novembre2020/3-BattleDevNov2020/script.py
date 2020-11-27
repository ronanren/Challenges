import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
res = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tete = [0]
for i in range(1, 10):
    futurtete = []
    for line in lines[1:]:
        if (int(line.split(" ")[1]) in tete):
            res[i] += 1
            futurtete.append(int(line.split(" ")[0]))
    tete = futurtete
    
print (" ".join([str(i) for i in res]))