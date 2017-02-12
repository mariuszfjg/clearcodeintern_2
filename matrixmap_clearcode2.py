from module_clearcode2 import *

mapDict=get_maps('map_input.txt')
mapDict=change_values_to_int(mapDict)
min_effort = init_effort(len(mapDict)) #init minimal effort list
