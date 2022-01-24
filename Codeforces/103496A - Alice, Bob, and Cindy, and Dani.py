names = input()
names = names.split(' ')
allNames = ['Alice', 'Bob', 'Cindy', 'Dani']

list_difference = [item for item in allNames if item not in names]
print(list_difference[0])