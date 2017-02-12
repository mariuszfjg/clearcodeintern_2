#gettin all maps/matrixes from file
#and putting it into dictionary
def get_maps(sourcename):
    map_source = open(sourcename,'r')
    lines = map_source.read().split('\n')
    l_cours = 0 #init line coursor
    m_size = int(lines[l_cours]) #actual matrix/map size
    dict_counter = 1
    fileDict = {}

    while l_cours<len(lines) and isinstance(m_size, int):
        values = []
        for i in range(l_cours,l_cours+m_size):
            values.append(lines[i+1].split(','))
        map_name = str(dict_counter)+'_'+str(m_size) #name of map - No._size
        fileDict[map_name] = values

        dict_counter+=1
        l_cours+=(m_size+1)
        m_size = lines[l_cours]
        try:
            m_size = int(m_size)
        except ValueError:
            print('Read',dict_counter-1,'maps')
            print("Couldn't set another map size. Propably reached EOF.")
            print(5*'x','finished reading file',5*'x')
            print('')
            break

    map_source.close()
    return fileDict
#changing all values from string to int in dictionary
#containing maps
def change_values_to_int(inputDict):
    for i in inputDict.keys():
        for j in range(0,len(inputDict[i])):
            for k in range(0,len(inputDict[i][j])):
                inputDict[i][j][k]=int(inputDict[i][j][k])
    return inputDict
#initializing list where minimal effort will be stored
def init_effort(list_len):
    effort_list = []
    for i in range (0,list_len):
        effort_list.append(0)

    return effort_list
