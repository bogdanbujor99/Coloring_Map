from Map import Map
from Country import Country
from Forward_checking import Forward_checking

A = Country("A")
B = Country("B")
C = Country("C")
D = Country("D")
A.set_neighbor([B,C])
B.set_neighbor([A,C])
C.set_neighbor([A,B])
D.set_neighbor([])
A.list_colors = ["blue","red","yellow"]
B.list_colors = ["red","blue"]
C.list_colors = ["red","blue"]
D.list_colors = ["red"]
list_countries = [A,B,C,D]
map = Map(list_countries)
if Forward_checking(map) == 0 :
    print("Nu exista solutie")