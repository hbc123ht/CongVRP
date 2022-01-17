from CongVRP import GeneticVRP
from CongVRP import City

from numpy import genfromtxt


coor = genfromtxt('./test_data/test_data_30.csv', delimiter=',')

cityList = []

for i in range(0,30):
    cityList.append(City(x=coor[i][0], y=coor[i][1], id = i))
    
def distance_callback(cityA, cityB):
    xDis = abs(cityA.x - cityB.x)
    yDis = abs(cityA.y - cityB.y)
    distance = xDis + yDis
    return distance

geneticAlgorithm = GeneticVRP()
geneticAlgorithm = geneticAlgorithm.RegisterTransitCallback(distance_callback)

path = geneticAlgorithm.geneticAlgorithm(population=cityList, popSize=50, eliteSize=10, mutationRate=0.01, generations=500)