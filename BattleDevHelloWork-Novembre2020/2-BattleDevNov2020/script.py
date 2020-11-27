import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
res = [0, 0] # [OK, SUSPICIOUS]
for time in lines[1:]:
    if (int(time[0:2]) >= 20 or int(time[0:2]) < 8):
        res[1] += 1
    else:
        res[0] += 1
    
print ("OK" if res[0] > res[1] else "SUSPICIOUS")