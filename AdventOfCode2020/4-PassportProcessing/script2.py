import sys, re

lines = []
for line in sys.stdin:
    lines.append(line)

passports = [] 
temp = {}   
for i, line in enumerate(lines):
    if (line != "\n"):
        for j in line.split(" "):
            temp[j.split(':')[0]] = j.split(':')[1].replace("\n", "")
    else:
        passports.append(temp)
        temp = {}
    if (i + 1 == len(lines)):
        passports.append(temp)
    
def byr(i):
    res = False
    if (i.get("byr", "false").isdigit()):
        if (1920 <= int(i.get("byr")) <= 2002):
            res = True
    return res

def iyr(i):
    res = False
    if (i.get("iyr", "false").isdigit()):
        if (2010 <= int(i.get("iyr")) <= 2020):
            res = True
    return res

def eyr(i):
    res = False
    if (i.get("eyr", "false").isdigit()):
        if (2020 <= int(i.get("eyr")) <= 2030):
            res = True
    return res

def hgt(i):
    res = False
    if (i.get("hgt", False)):
        if (i.get("hgt")[-2:] == "cm"):
            if (i.get("hgt")[:3].isdigit() and 150 <= int(i.get("hgt")[:3]) <= 193):
                res = True
        elif (i.get("hgt")[-2:] == "in"):
            if (i.get("hgt")[:2].isdigit() and 59 <= int(i.get("hgt")[:2]) <= 76):
                res = True
    return res

def hcl(i):
    res = False
    if (i.get("hcl", False) and bool(re.match(r'#[0-9a-f]{6}', i.get("hcl")))):
        res = True
    return res

def ecl(i):
    res = False
    if (i.get("ecl", False) and i.get("ecl") in ["amb","blu","brn","gry","grn","hzl","oth"]):
        res = True
    return res

def pid(i):
    res = False
    if (i.get("pid", False) and i.get("pid").isdigit() and len(i.get("pid").replace("\n", "")) == 9):
        res = True
    return res

res = 0
for passport in passports:
    if(byr(passport) and iyr(passport) and eyr(passport) and hgt(passport) and hcl(passport) and ecl(passport) and pid(passport)):
        res += 1
        
print (res)