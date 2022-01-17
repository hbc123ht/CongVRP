import numpy as np
from sklearn.cluster import KMeans
from CongVRP.model import Cluster

def get_bit(bitmask:int, pos:int):
    """
    """
    return (bitmask >> (pos)) & 1

def on_bit(bitmask:int, pos:int):
    """
    """
    return bitmask + (1 << pos)

def off_bit(bitmask:int, pos:int):
    """
    """
    return bitmask - (1 << pos)

def count_bit(bitmask:int):
    """
    """
    cnt = 0
    for id in range(70):
        if get_bit(bitmask, id):
            cnt = cnt + 1
        
    return cnt
  
def clustering(cluster, n_clusters):

    coor = []
    for city in cluster.city_list:
        coor.append([city.x, city.y])

    kmeans = KMeans(n_clusters=n_clusters, random_state=5).fit(coor)

    cluster_list = [Cluster() for _ in range(n_clusters)]

    for id, label in enumerate(kmeans.labels_):
        cluster_list[label].append(cluster.city_list[id])
    
    return cluster_list

def create_distance(cluster_list, distance_callback):
    """
    """
    n = len(cluster_list)
    distance = [[0] * n for i in range(n)]

    for id in range(n):
        for id_ in range(n):
            distance[id][id_], _ = cluster_list[id].distance(cluster_list[id_], distance_callback)

    return distance

def find_optimal_path(distance:list, start, end):
    """
    """

    # the number of nodes
    num_node = len(distance)
    # num bitmask presented for number of situations
    num_bitmask = (1 << num_node)
    # initiate dp
    dp = [[1e9] * num_node for i in range(num_bitmask)]

    dp[on_bit(0, start)][start] = 0

    # find dp
    for current_bitmask in range(num_bitmask):
        for current_node in range(num_node):
            # whether current_node has been visited
            if get_bit(current_bitmask, current_node) == 1:
                for next_node in range(num_node):
                    # whether next_node has been visited
                    if get_bit(current_bitmask, next_node) == 0:
                        # bitmask after visiting current_node
                        next_bitmask = on_bit(current_bitmask, next_node)

                        # update dp
                        dp[next_bitmask][next_node] = min(dp[next_bitmask][next_node], \
                        dp[current_bitmask][current_node] + distance[current_node][next_node])

    min_cost = np.inf
    end_point = None
    path = []

    if (start == end):
        path.append(end)
        for i in range(num_node):
            if min_cost > dp[num_bitmask - 1][i] + distance[i][end]:
                min_cost = min(min_cost, dp[num_bitmask - 1][i] + distance[i][end])
                end_point = i
    else:
        end_point = end
        min_cost = dp[num_bitmask - 1][end]

    # trace the path
    current_bitmask = num_bitmask - 1

    while (count_bit(current_bitmask) > 1):
        path.append(end_point)
        for i in range(num_node):
            if i != end_point and (get_bit(current_bitmask, i)):
                # previous bit mask
                pre_bitmask = off_bit(current_bitmask, end_point)
                if dp[pre_bitmask][i] + distance[i][end_point] == dp[current_bitmask][end_point]:
                    current_bitmask = pre_bitmask
                    end_point = i
                    break

    path.append(start)
    path.reverse()

    return (path, min_cost)

def find_nearest_city(newCity, path, distance_callback, pos_city_added = None, city_type = None):
    minCost = np.inf
    pos = None

    if city_type == "drop":
        for id, city in enumerate(path):
            if id <= pos_city_added or id == 0:
                continue
            distance = distance_callback(city, newCity)
            if distance < minCost:
                minCost = distance
                pos = id
    elif city_type == 'pickup':
        for id, city in enumerate(path):
            if id > pos_city_added or id == 0:
                continue
            distance = distance_callback(city, newCity)
            if distance < minCost:
                minCost = distance
                pos = id
    else:
        for id, city in enumerate(path):
            distance = distance_callback(city, newCity)
            if id == 0:
                continue
            if distance < minCost:
                minCost = distance
                pos = id

    return pos

def add_city(path, pos, city):
    new_path = path[:pos]
    new_path.append(city)
    new_path = new_path + path[pos:]
    return new_path

def edit(path, pickupCity, dropCity, distance_callback):
    #remove those cities first
    for city in path:
        if city.id == pickupCity: 
            pickupCity = city
            path.remove(city)
            break
    for city in path:
        if city.id == dropCity:
            dropCity = city
            path.remove(city)
            break
    # print(pickupCity, dropCity)
    pos = find_nearest_city(pickupCity, path, distance_callback)
    path = add_city(path, pos, pickupCity)
    pos = find_nearest_city(dropCity, path, distance_callback, pos_city_added=pos, city_type='drop')
    path = add_city(path, pos, dropCity)

    return path



