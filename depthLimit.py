def depth_limited_search(graph, start_node, goal_node, depth_limit):
    # Visited set to keep track of explored nodes
    visited = set()
    path = []  # List to store the path taken

    def recursive_search(node, depth):

        if depth == depth_limit or node == goal_node:
            path.append(node)
            return node == goal_node

        # Mark node as visited
        visited.add(node)
        path.append(node)  # Add current node to path

        # Explore unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Perform recursive search on neighbor
                if recursive_search(neighbor, depth + 1):
                    return True

        # Backtrack (remove current node from path if goal not found at this branch)
        path.pop()
        return False

    # Start the search from the starting node
    if recursive_search(start_node, 0):
        print("Goal node found within depth limit. Path:", path)
    else:
        print("Goal node not found within depth limit")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': ['H']
}

start_node = 'A'
goal_node = 'G'
depth_limit = 3

depth_limited_search(graph, start_node, goal_node, depth_limit)
