from module_clearcode2 import *

mapDict=get_maps('map_input.txt')
mapDict=change_values_to_int(mapDict)

maps_par=get_maps_par(mapDict)
for i in range(1,len(maps_par)):
    name=str(maps_par[i][0])+'_'+str(maps_par[i][1])
    print(main_effort(mapDict[name],maps_par[i][1]))
