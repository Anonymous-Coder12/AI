#A star search
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
pq=PriorityQueue()
visited=set()
pq.put((H[startnode]+0,startnode))
path=[]
ans=0
while (pq.empty()==False):
    f,node=pq.get()
    visited.add(node)
    path.append(node)
    costuptoit=f-H[node]
    ans=costuptoit
    if (node==goalnode):
        break
    for neighbour in graph[node]:
        if neighbour[0] not in visited:
            pq.put((costuptoit+neighbour[1]+H[neighbour[0]],neighbour[0]))
    

print(path)
print(ans)

        
            
