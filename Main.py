from Map import Map
from Country import Country
from Forward_checking import Forward_checking

A = Country("A")
B = Country("B")
C = Country("C")
A.set_neighbor([B,C])
B.set_neighbor([A,C])
C.set_neighbor([A,B])
A.list_colors = ["red"]
B.list_colors = ["red","blue","yellow"]
C.list_colors = ["red","blue"]
list_countries = [A,B,C]
map = Map(list_countries)
if Forward_checking(map) == 0 :
    print("Nu exista solutie")