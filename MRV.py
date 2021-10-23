def MRV(M):
    country = None
    for x in M.list_countries:
        if x.color_set == "":
            country = x
            break
    if country == None:
        return None
    min = len(country.list_colors)
    for i in M.list_countries:
        if min > len(i.list_colors) and len(i.list_colors)>0:
            min = len(i.list_colors)
            country = i
    return country

