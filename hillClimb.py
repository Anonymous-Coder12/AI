# import random
# import math

# # Coordinates of the cities
# coordinates = [[1, 2], [30, 21], [56, 23], [8, 18], [20, 50], [3, 4], [11, 6], [6, 7], [15, 20], [10, 9], [12, 12]]

# # Generate the distance matrix based on the coordinates
# def generate_distance_matrix(coordinates):
#     num_cities = len(coordinates)
#     distance_matrix = [[0 for _ in range(num_cities)] for _ in range(num_cities)]
#     for i in range(num_cities):
#         for j in range(num_cities):
#             distance_matrix[i][j] = math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
#     return distance_matrix

# # Generate a random initial solution
# def generate_random_solution(num_cities):
#     return random.sample(range(num_cities), num_cities)

# # Calculate the total path length of a solution
# def calculate_path_length(solution, distance_matrix):
#     path_length = 0
#     for i in range(len(solution)):
#         path_length += distance_matrix[solution[i-1]][solution[i]]
#     return path_length

# # Generate neighbors by swapping two cities in the solution
# def generate_neighbors(solution):
#     neighbors = []
#     for i in range(len(solution)):
#         for j in range(i+1, len(solution)):
#             neighbor = solution.copy()
#             neighbor[i] = solution[j]
#             neighbor[j] = solution[i]
#             neighbors.append(neighbor)
#     return neighbors

# # Perform hill climbing to find the best solution
# def hill_climbing(coordinates):
#     distance_matrix = generate_distance_matrix(coordinates)
#     num_cities = len(coordinates)
#     current_solution = generate_random_solution(num_cities)
#     current_path_length = calculate_path_length(current_solution, distance_matrix)

#     while True:
#         neighbors = generate_neighbors(current_solution)
#         best_neighbor = min(neighbors, key=lambda x: calculate_path_length(x, distance_matrix))
#         best_neighbor_path_length = calculate_path_length(best_neighbor, distance_matrix)
#         if best_neighbor_path_length >= current_path_length:
#             break
#         current_solution = best_neighbor
#         current_path_length = best_neighbor_path_length

#     return current_solution, current_path_length

# # Perform the hill climbing algorithm
# final_solution, path_length = hill_climbing(coordinates)
# print("The final solution is:", final_solution)
# print("The path length is:", path_length)


import random
import math

# Coordinates of the cities
coordinate = [[1, 2], [30, 21], [56, 23], [8, 18], [20, 50],
              [3, 4], [11, 6], [6, 7], [15, 20], [10, 9], [12, 12]]


def generate_matrix(coordinate):
    matrix = []
    for i in range(len(coordinate)):
        row = []
        for j in range(len(coordinate)):
            p = math.sqrt((coordinate[i][0] - coordinate[j][0])
                          ** 2 + (coordinate[i][1] - coordinate[j][1])**2)
            row.append(p)
        matrix.append(row)
    return matrix


def solution(matrix):
    points = list(range(0, len(matrix)))
    solution = []
    for i in range(0, len(matrix)):
        random_point = points[random.randint(0, len(points) - 1)]
        solution.append(random_point)
        points.remove(random_point)
    return solution


def path_length(matrix, solution):
    cycle_length = 0
    for i in range(0, len(solution)):
        cycle_length += matrix[solution[i]][solution[i - 1]]
    return cycle_length


def neighbors(matrix, solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)

    # Assume that the first neighbor in the list is the best neighbor
    best_neighbor = neighbors[0]
    best_path = path_length(matrix, best_neighbor)

    # Check if there is a better neighbor
    for neighbor in neighbors:
        current_path = path_length(matrix, neighbor)
        if current_path < best_path:
            best_path = current_path
            best_neighbor = neighbor
    return best_neighbor, best_path


def hill_climbing(coordinate):
    matrix = generate_matrix(coordinate)

    current_solution = solution(matrix)
    current_path = path_length(matrix, current_solution)
    neighbor = neighbors(matrix, current_solution)[0]
    best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)

    while best_neighbor_path < current_path:
        current_solution = best_neighbor
        current_path = best_neighbor_path
        neighbor = neighbors(matrix, current_solution)[0]
        best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)

    return current_path, current_solution


final_solution = hill_climbing(coordinate)
print("best cost:\n", final_solution[0])
print("The solution is \n", final_solution[1])
