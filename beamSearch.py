import heapq


def beam_search(start, goal, graph, beam_width):
    beam = [(0, [start])]
    while True:
        new_beam = []
        for cost, path in beam:
            current_node = path[-1]
            if current_node == goal:
                return path
            for neighbor, neighbor_cost in graph[current_node]:
                new_cost = cost + neighbor_cost
                new_path = path + [neighbor]
                heapq.heappush(new_beam, (new_cost, new_path))
        beam = heapq.nsmallest(beam_width, new_beam)


graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('C', 1), ('D', 3)],
    'C': [('D', 1)],
    'D': [('E', 2)],
    'E': []
}
start_node = 'A'
goal_node = 'E'
beam_width = 2
shortest_path = beam_search(start_node, goal_node, graph, beam_width)
print("Shortest path found:", shortest_path)
