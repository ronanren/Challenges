import sys

lines = []
for line in sys.stdin:
    lines.append(line.replace("\n", ""))

bags = {}
for i in lines:
    bag = i.split(" contain")[0]
    bags[bag] = [j.strip() for j in i.split(" contain")[1].split(", ")]


def recursive(bags, my_bag="shiny gold", array=[]):
    for key, value in bags.items():
        for j in value:
            if my_bag in j and key not in array:
                array.append(key)          
                recursive(bags, my_bag=key)
    return array

print(len(recursive(bags)))