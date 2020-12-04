import sys

lines = []
for line in sys.stdin:
    lines.append(line)

passports = [] 
temp = {}   
for i, line in enumerate(lines):
    if (line != "\n"):
        for j in line.split(" "):
            temp[j.split(':')[0]] = j.split(':')[1]
    else:
        passports.append(temp)
        temp = {}
    if (i + 1 == len(lines)):
        passports.append(temp)
    
res = 0
for passport in passports:
    if (passport.get("byr", False) and passport.get("iyr", False) and passport.get("eyr", False) and passport.get("hgt", False) and passport.get("hcl", False) and
        passport.get("ecl", False) and passport.get("pid", False)):
        res += 1
        
print (res)