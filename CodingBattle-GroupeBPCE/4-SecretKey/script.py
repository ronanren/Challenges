import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

suite = lines[1]
approche = lines[2]
diff = len(suite)

def diff_letters(a, b):
    return sum(a[i] != b[i] for i in range(len(a)))

def droite(i):
	alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	return i[1:] + alpha[alpha.index(i[-1:]) + 1]

def gauche(i):
	return i[1:] + i[0]
