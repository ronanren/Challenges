import sys

lines = {}
for line in sys.stdin:
    lines[line.replace("\n", "").split(" contain ")[0]] = line.replace("\n", "").split(" contain ")[1].split(", ")

def recursive(lines, bags, res=[]):
    tempbag = []
    
    for bg, listbag in lines.items():
        for bag in bags:
            for j in listbag:   
                if bag in j and bg not in res:
                    tempbag.append(bg)
                    res.append(bg)
    print(len(res))
    if tempbag != []:
        recursive(lines, tempbag, res)

recursive(lines, ['shiny gold'])