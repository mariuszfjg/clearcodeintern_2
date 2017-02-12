def get_maps(sourcename):
    lines = open(sourcename,'r').read().split('\n')
    l_cours = 0 #init line coursor
    m_size = int(lines[l_cours]) #actual matrix size
    dict_counter = 1
    fileDict = {}

    while l_cours<len(lines) and isinstance(m_size, int):
        values = []
        for i in range(l_cours,l_cours+m_size):
            values.append(lines[i+1].split(','))
        fileDict[str(dict_counter)] = values

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

    return fileDict
