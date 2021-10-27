class Country:
    def __init__(self,name):
        self.name = name
        self.color_set = ""
        self.color_choose = -1
        self.list_colors =  []
        self.list_neighbor = []

    def set_neighbor(self,list_neighbor):
        self.list_neighbor = list_neighbor