import numpy as np

class City:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
    
    def __repr__(self):
        return "(" + str(self.id) + ")"

class Cluster:
    def __init__(self, city_list = None):
        self.city_list = []
        if (city_list != None):
            self.city_list = city_list
    
    def get_quantity(self):
        return len(self.city_list)

    def append(self, city):
        self.city_list.append(city)

    def distance(self, cluster, distance_callback):
        min_distance = np.inf
        city_list = cluster.city_list
        connect_city = None
        
        for beg in self.city_list:
            for des in city_list:
                distance = distance_callback(beg, des)
                if min_distance > distance:
                    min_distance = distance
                    connect_city = beg.id
        
        return min_distance, connect_city

