from .city import City

def read_data(filepath):
    with open(filepath, 'r') as f:
        data = f.readlines()[6:-1]
        data = [list(map(int, line.strip().split())) for line in data]
        data = [City(*city_data) for city_data in data]
    
    return data


def create_distance_matrix(data):
    size = len(data)

    matrix = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j] = matrix[j][i] = data[i].get_distance(data[j])

    return matrix


def get_instance(filepath):
    data = read_data(filepath)
    distance_matrix = create_distance_matrix(data)

    return distance_matrix