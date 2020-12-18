import sys, re
sys.setrecursionlimit(10000)

lines = []
for line in sys.stdin:
    lines.append(line.replace(" ", "").replace("\n", ""))

def calcul(expr):
    for j in range(5, 50):
        for i in range(j, len(expr)+1):
            if (re.match(r"\(\d+[\+\-\*]\d+\)", expr[i-j:i])):
                expr = expr.replace(expr[i-j:i], str(eval(expr[i-j:i])))
   
    if (expr.count('(') > 0):
        return calcul(expr)
    else:
        return eval(expr)



for expr in lines:
    print(calcul(expr))