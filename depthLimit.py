graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':['G'],
    'G':['H']
}
#adjacency list is stored in form of dictionary with node ===> list mapping
#in dls dfs is performed upto a certain limit only
startnode='A'
goalnode='G'
depthlimit=3
#assumed that search will go only upto level number <=3

path=[]
visited=set()

def searchit(start,depth):
    if (depth>depthlimit):
        return False;
    if (start==goalnode):
        path.append(start)
        return True;
    visited.add(start)
    path.append(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            foundornot=searchit(neighbour,depth+1)
            if (foundornot):
                return True;
    path.pop()
    visited.pop()
    return False;


print("PRESENT OR NOT:- ",searchit(startnode,0))
print(path)
    
            






