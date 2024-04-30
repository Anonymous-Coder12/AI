#BEST FIRST SEARCH
from queue import PriorityQueue
H= {
    'A': 11,
    'B': 6,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
     'J': 0
}
graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    'J':[]
}
startnode='A'
goalnode='J'

visited=set()
path=[]
pq=PriorityQueue()
visited.add(startnode)
pq.put((H['A'],'A'))
dist=0
prevnode='A'
while(pq.empty()==False):
    heu,u=pq.get()
    path.append(u)
    prevnode=u
    if (u==goalnode):
        break
    for neighbour in graph[u]:
        if neighbour[0] not in visited:
            visited.add(neighbour[0])
            pq.put((H[neighbour[0]],neighbour[0]))

for i in range(1,len(path)):
    u=path[i-1]
    v=path[i]
    for first in graph[u]:
        if (first[0]==v):
            dist+=first[1]
            break
print("DISTANCE IS :- ",dist)
print(path)
    


