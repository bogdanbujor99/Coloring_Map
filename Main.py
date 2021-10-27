from Map import Map
from Country import Country
from Forward_checking import Forward_checking

A = Country("A")
B = Country("B")
C = Country("C")
D = Country("D")
A.set_neighbor([B,C])
B.set_neighbor([A,C])
C.set_neighbor([A,B,D])
D.set_neighbor([C])
A.list_colors = ["red","blue"]
B.list_colors = ["red"]
C.list_colors = ["red","yellow"]
D.list_colors = ["yellow","red","blue"]
list_countries = [A,B,C,D]
map = Map(list_countries)
if Forward_checking(map) == 0 :
    print("Nu exista solutie")