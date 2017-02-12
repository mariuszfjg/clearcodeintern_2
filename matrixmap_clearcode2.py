lines = open('map_input.txt','r').read().split('\n')
n = int(lines[0])
l_cours = 0
dict_counter = 1
fileDict = {}

values = []
for i in range(l_cours,l_cours+n):
    values.append(lines[i+1].split(','))
fileDict[str(dict_counter)] = values

print(fileDict)

lines.close()
