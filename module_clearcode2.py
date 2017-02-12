######### GENERAL OPERATIONS #########
def get_maps_par(mapDict):
    par=[]
    par.append(0)
    for k in mapDict.keys():
        size = int(k[len(k)-1])
        name = ''
        for i in range(0,len(k)-2):
            name+=str(k[i])
        par.insert(int(name),[int(name),size])
    return par
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
            # print('Read',dict_counter-1,'maps')
            # print("Couldn't set another map size. Propably reached EOF.")
            # print(5*'x','finished reading file',5*'x')
            # print('')
            break

    map_source.close()
    return fileDict
#changing all values from string to int in dictionary
#containing maps
def change_values_to_int(inputDict):
    for k in inputDict.keys():
        for i in range(0,len(inputDict[k])):
            for j in range(0,len(inputDict[k][i])):
                inputDict[k][i][j]=int(inputDict[k][i][j])
    return inputDict
#initializing list where minimal effort will be stored

######### OPERATIONS ON MAPS #########

#select n x n map as part from input maplist
#starting from maplist[r][c]
def smaller_map(n,map_list,r,c):
    s_map=[]
    for i in range(0,n):
        s_map.append([])
        for j in range(0,n):
            s_map[i].append(map_list[i+r][j+c])

    return s_map
#counting effort for 2x2 map
def effort_2(maplist):
    if maplist[1][0]>maplist[0][1]:
        return maplist[0][0]+maplist[1][1]+maplist[0][1]
    else:
        return maplist[0][0]+maplist[1][1]+maplist[1][0]
#counting effort for 3x3 map
def effort_3(maplist):
    upper_diag = effort_2(smaller_map(2,maplist,0,1))
    lower_diag = effort_2(smaller_map(2,maplist,1,0))
    if upper_diag<lower_diag:
        return upper_diag+maplist[0][0]+maplist[2][2]
    else:
        return lower_diag+maplist[0][0]+maplist[2][2]
#counting effort for 4x4, 5x5,.... maps
#maplist - 2D list of values from map
#n - size of the map
def effort_gt3(maplist,n):
    cons_points=maplist[0][0]+maplist[n-1][n-1]
    if n==4:
        upper_diag = effort_3(smaller_map(3,maplist,0,1))
        lower_diag = effort_3(smaller_map(3,maplist,1,0))
        if upper_diag<lower_diag:
            return upper_diag+cons_points
        else:
            return lower_diag+cons_points
    else:
        upper_diag = effort_gt3(smaller_map(n-1,maplist,0,1),n-1)
        lower_diag = effort_gt3(smaller_map(n-1,maplist,1,0),n-1)
        if upper_diag<lower_diag:
            return upper_diag+cons_points
        else:
            return lower_diag+cons_points
#main function distributing counting effort
#Selecting function to make problem easy when it's possible
#maplist - 2D list, size - size of map
def main_effort(maplist,size):
    if size>0:
        if size==1:
            return maplist[0][0]
        elif size==2:
            return effort_2(maplist)
        elif size==3:
            return effort_3(maplist)
        elif size>3:
            return effort_gt3(maplist,size)
