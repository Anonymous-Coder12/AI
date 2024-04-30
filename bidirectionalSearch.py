from queue import Queue
sourcevis=set()
destvis=set()
graph={
    'A':['B','C'],
    'B':['D','E','A'],
    'C':['F'],
    'D':[],
    'E':['F','B'],
    'F':['G','E'],
    'G':['H','F'],
    'H':[]
}
vertices=['A','B','C','D','E','F','G','H']
startnode='A'
goalnode='G'
sourceparent={}
destparent={}
sourcequeue=Queue()
destqueue=Queue()
def bidirsearch(startnode,goalnode):
    sourcequeue.put(startnode)
    destqueue.put(goalnode)
    sourcevis.add(startnode)
    destvis.add(goalnode)
    while sourcequeue.empty()==False and destqueue.empty()==False:
        u=sourcequeue.get()
        for sourceneighbour in graph[u]:
            if sourceneighbour not in sourcevis:
                sourcevis.add(sourceneighbour)
                sourcequeue.put(sourceneighbour)
                sourceparent[sourceneighbour]=u
        v=destqueue.get()
        for destneighbour in graph[v]:
            if destneighbour not in destvis:
                destvis.add(destneighbour)
                destqueue.put(destneighbour)
                destparent[destneighbour]=v
        for i in vertices:
          if (i in destvis) and (i in sourcevis):
              path=[]
              path.append(i)
              temp=i
              while(temp!=startnode):
                  temp=sourceparent[temp]
                  path.append(temp)
              path.reverse()
              temp=i
              while(temp!=goalnode):
                  temp=destparent[temp]
                  path.append(temp)
              return path
print(bidirsearch(startnode,goalnode))
    
