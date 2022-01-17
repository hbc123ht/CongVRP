from CongVRP import CongVRP
from CongVRP import Cluster, City

from numpy import genfromtxt

# Read coor
coor = genfromtxt('./test_data/test_data_30.csv', delimiter=',')

#init Cluster
cluster = Cluster()

# add City objects into the cluster object
for i in range(0,30):
    cluster.append(City(x=coor[i][0], y=coor[i][1], id = i))

# define a function for calculation distance between 2 City objects
def distance_callback(cityA, cityB):
    xDis = abs(cityA.x - cityB.x)
    yDis = abs(cityA.y - cityB.y)
    distance = xDis + yDis
    return distance


CongVRP = CongVRP()

# Register distance function
CongVRP.RegisterTransitCallback(distance_callback)

# Add constraints PickupandDrop
CongVRP.AddPickupAndDelivery(21, 19)
CongVRP.AddPickupAndDelivery(7, 18)

# find route
department = 0
destination = 0
path = CongVRP.find_route(cluster, department, destination)

print(path)
