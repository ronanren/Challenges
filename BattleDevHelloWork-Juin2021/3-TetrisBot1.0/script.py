import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

def verifLigne(ligne, colonne):
	verif = True
	for i in range(0, 10):
		if (lines[ligne][i] != '#' and i != colonne):
			verif = False
			break
	for i in range(ligne, -1, -1):
		if (lines[i][colonne] != '.'):
			verif = False
			break
	return verif

res = "NOPE"
for i in range(0, 10):
	for j in range(16, -1, -1):
		if (lines[j][i] == '.' and lines[j+1][i] == '.' and lines[j+2][i] == '.' and lines[j+3][i] == '.'):
			if (verifLigne(j, i)  & verifLigne(j+1, i) & verifLigne(j+2, i) & verifLigne(j+3, i)):
				if (j + 4 == 20 or lines[j+4][i] == '#'):
					res = "BOOM " + str(i+1)
					break
print(res)