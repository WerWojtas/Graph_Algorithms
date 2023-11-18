import sys
sys.path.append("C:\\Users\\weron\\OneDrive\\Pulpit\\Grafowe")
from time import sleep

class RecursionTimeoutError(Exception): # Błąd rekurencji
    pass

def residual(G,Parent,vertex,max_flow):
    while Parent[vertex]!=None:
        for i in range(len(G[Parent[vertex]])):
            if G[Parent[vertex]][i][0]==vertex:
                G[Parent[vertex]][i][1]-=max_flow
                break
        for i in range(len(G[vertex])):
            if G[vertex][i][0]==Parent[vertex]:
                G[vertex][i][1]+=max_flow
                break
        vertex = Parent[vertex]

    

def ford_fulkerson(my_graph,s):
    G = my_graph.change_representation_residual(0,len(my_graph.edges)-1)
    s = s-1
    t = len(G) -1
    max_depth = 1000
    Parent = [None]*len(G)
    Visited = [False] * len(G)
    
    flow=0

    def DFS_visit(G, vertex, max_flow, depth):
        Visited[vertex] = True
        nonlocal t, max_depth, flow
        if depth > max_depth:
            raise RecursionTimeoutError("Przekroczono maksymalną głębokość rekurencji")
        if vertex == t:
            residual(G,Parent,vertex,max_flow)
            flow+=max_flow
            return True
        for edge in G[vertex]:
            neighbour = edge[0]
            if edge[1] > 0 and Visited[neighbour] == False:
                Parent[neighbour] = vertex
                if max_flow > edge[1]:
                    max_flow = edge[1]
                if DFS_visit(G, edge[0], max_flow, depth +1):
                    return True
        return False
    
    while DFS_visit(G,s,float('inf'), 0):
        Visited = [False] * len(G)
        Parent = [None]*len(G)


    return flow


T = [(1,3,6),(1,4,3),(3,4,1),(3,5,2),(3,6,2),(4,6,1),(4,5,2),(6,5,2),(5,2,4),(6,2,4)]


        
                    
    
