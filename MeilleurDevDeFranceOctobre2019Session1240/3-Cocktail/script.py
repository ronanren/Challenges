import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

res = [] 
for i in lines[1:]:
	if (i.split(" ")[1] in res):
		if (i.split(" ")[0] not in res):
			res.insert(res.index(i.split(" ")[1]), i.split(" ")[0])
		else:
			res.append(i.split(" ")[0])
	else:
		if (i.split(" ")[0] not in res):
			res.append(i.split(" ")[0])
		if (i.split(" ")[1] not in res):
			res.append(i.split(" ")[1])

valid = True
for i in res:
	if (res.count(i) > 1):
		valid = False
if valid:
	print (" < ".join([str(i) for i in res]))
else:
	print ("KO")