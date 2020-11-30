import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

dic = {}
for i in lines[1:]:
    if (dic.get(i.split(" ")[1], False)):
        dic[i.split(" ")[1]] += 1
    else:
        dic[i.split(" ")[1]] = 1

for key, value in dic.items():
    if (value == 1):
        for i in lines[1:]:
            if (i.split(" ")[1] == key):
                res = i.split(" ")[0]
print (res)
