def add_city(path, pos, city):
    new_path = path[:pos]
    new_path.append(city)
    new_path = new_path + path[pos:]
    return new_path

x = [1, 2, 3]
x = add_city(x, 1, -1)
print(x)

