import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

gammaRate = ""
for column in range(0, len(lines[0])):
	bits0 = 0
	bits1 = 0
	for line in lines:
		if (line[column] == "0"):
			bits0 += 1
		else:
			bits1 += 1
	if (bits1 > bits0):
		gammaRate += "1"
	else:
		gammaRate += "0"

epsilonRate = gammaRate.replace("0", "2").replace("1", "0").replace("2", "1")
print(int(gammaRate, 2) * int(epsilonRate, 2))
