import sys, math

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

def toString(horaire):
	if (horaire == 1440):
		return "00:00"
	return str('{:0>2}'.format(math.floor(horaire/60))) + ":" + str('{:0>2}'.format(horaire % 60))

tab = [0] * 60 * 24
horaire1 = 0
horaire2 = 0
horairetemp1 = 0
horairetemp2 = 0
max = 0
maxtemp = 0

for i in lines[1:]:
	time1 = int(i.split("-")[0].replace(":", ""))
	time2 = int(i.split("-")[1].replace(":", ""))
	for j in range(time1, time2):
		tab[int(j - ((j - j % 100)/100 * 40))] = 1

for i, value in enumerate(tab):
	if value == 0:
		maxtemp += 1
		horairetemp2 = i
		if maxtemp == 1:
			horairetemp1 = i
		if maxtemp > max:
			max = maxtemp
			horaire1 = horairetemp1
			horaire2 = horairetemp2
		if i + 1 == len(tab):
			j = 0
			while tab[j] == 0:
				maxtemp += 1
				horairetemp2 = j
				j += 1
				if maxtemp > max:
					max = maxtemp
					horaire1 = horairetemp1
					horaire2 = horairetemp2
				
	else:
		maxtemp = 0
	
print (toString(horaire1 + 1) + "-" + toString(horaire2))