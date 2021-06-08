import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

def split(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out

orbit = [element for element in lines[1]]
elements = list(set(orbit))
minimum = 1000
for elem in elements:
	if (minimum > orbit.count(elem)):
		minimum = orbit.count(elem)

res = 0
for i in range(0, len(orbit)):
	equal = True
	arrays = split(orbit, minimum)
	if (minimum == 2):
		if sorted(arrays[0]) != sorted(arrays[1]):
			equal = False
	if (minimum == 3):
		if sorted(arrays[0]) != sorted(arrays[1]) or sorted(arrays[0]) != sorted(arrays[2]) or sorted(arrays[1]) != sorted(arrays[2]):
			equal = False
	if (equal):
		# print(arrays)
		res += 1
	orbit.insert(0, orbit.pop())
	
print(res)
# NOT FINISHED