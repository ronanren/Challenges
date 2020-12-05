import sys

lines = []
for line in sys.stdin:
    lines.append(line)

def decrypt(seat, i, row, column):
    if (seat[i] == 'F'):
        row[1] = row[1] - int((row[1] - row[0] + 1) / 2)
        decrypt(seat, i + 1, row, column)
    elif (seat[i] == 'B'):
        row[0] = row[0] + int((row[1] - row[0] + 1) / 2)
        decrypt(seat, i + 1, row, column)
    elif (seat[i] == 'R'):
        column[0] = column[0] + int((column[1] - column[0] + 1) / 2)
        if (len(seat) - 1 > i):
            decrypt(seat, i + 1, row, column)
    elif (seat[i] == 'L'):
        column[1] = column[1] - int((column[1] - column[0] + 1) / 2)
        if (len(seat) - 1 > i):
            decrypt(seat, i + 1, row, column)
    return (row[0] * 8 + column[0]) 

res = []
for i in lines:
    res.append(decrypt(i, 0, [0, 127], [0, 7]))
    
res = sorted(res)
for i, seat in enumerate(res):
    if (i + 1 < len(res) and res[i+1] == seat + 2):
        result = seat + 1 

print(result)
