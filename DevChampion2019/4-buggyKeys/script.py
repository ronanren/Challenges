import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

character = [char for char in lines[-1]] 
translate = lines[1].split(" ")
translateTo = {}


for i in range(0, len(translate)):
	translateTo[translate[i]] = lines[2].split(" ")[i]

for i in range(0, len(character)):
	try :
		if character[i].isupper():
			character[i] = translateTo[character[i].lower()].upper()
		else:
			character[i] = translateTo[character[i]]
	except:
		pass


print ("".join([str(c) for c in character]))