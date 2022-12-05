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
            score += 4
        elif (me == 'Z'):
            score += 8
        else:
            score += 3
    elif (opponent == 'B'):
        if (me == 'Z'):
            score += 9
        elif (me == 'X'):
            score += 1
        else:
            score += 5
    elif (opponent == 'C'):
        if (me == 'X'):
            score += 2
        elif (me == 'Y'):
            score += 6
        else:
            score += 7
    sum_score += score

print(sum_score)
