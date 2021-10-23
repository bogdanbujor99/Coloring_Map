from MRV import MRV
import copy

def Forward_checking(map):
    map_original = copy.deepcopy(map)

    country = MRV(map)

    if country == None:
        return 1

    index = map.list_countries.index(country)

    map.list_countries[index].color_choose += 1
    map_original.list_countries[index].color_choose += 1
    
    if len(map.list_countries[index].list_colors) <= map.list_countries[index].color_choose:
        return 0
    
    map.list_countries[index].color_set = map.list_countries[index].list_colors[map.list_countries[index].color_choose]
    map.list_countries[index].list_colors = []

    for neighbor in map.list_countries[index].list_neighbor:
        exist = map.list_countries[index].color_set in neighbor.list_colors
        if exist :
            neighbor.list_colors.remove(map.list_countries[index].color_set)
    
    print("A=" + map.list_countries[0].color_set + " B=" + map.list_countries[1].color_set + " C=" + map.list_countries[2].color_set)

    if Forward_checking(map) == 1 :
        return 1
    elif Forward_checking(map_original) == 0 : 
        return 0

    

