from queue import PriorityQueue


def bestFirst(graph, src, target, n, hf):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, src))
    visited[src] = True
    cost = 0
    while pq.empty() == False:
        dist, u = pq.get()
        cost += dist
        print(u, end=" ")
        if u == target:
            break
        if (len(graph[u]) != 0):
            for v, c in graph[u]:
                if visited[v] == False:
                    visited[v] = True
                    pq.put((hf[v], v))
    print()
    return cost


v = 10
graph = [[] for i in range(v)]

hf = {1: 12, 2: 4, 3: 7, 4: 3, 5: 8, 6: 2, 7: 4, 8: 9, 9: 0}


def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


addedge(0, 1, 3)
addedge(0, 2, 2)
addedge(1, 3, 4)
addedge(1, 4, 1)
addedge(2, 5, 3)
addedge(2, 6, 1)
addedge(5, 7, 5)
addedge(6, 8, 2)
addedge(6, 9, 3)

source = 0
target = 9
print(bestFirst(graph, source, target, v, hf))
# p = PriorityQueue()
# p.put((5, 10))
# p.put((10, 1))
# p.put((1, 5))
# print(p.get())
