import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

sum_score = 0
for round in lines:
    opponent = round.split(' ')[0]
    me = round.split(' ')[1]
    score = 0
    if (opponent == 'A'):
        if (me == 'Y'):
            score += 8
        elif (me == 'Z'):
            score += 3
        else:
            score += 4
    elif (opponent == 'B'):
        if (me == 'Z'):
            score += 9
        elif (me == 'X'):
            score += 1
        else:
            score += 5
    elif (opponent == 'C'):
        if (me == 'X'):
            score += 7
        elif (me == 'Y'):
            score += 2
        else:
            score += 6
    sum_score += score

print(sum_score)
