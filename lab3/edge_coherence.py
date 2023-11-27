import sys
sys.path.append("C:\\Users\\weron\\OneDrive\\Pulpit\\Grafowe")
from collections import deque
from copy import deepcopy

class RecursionTimeoutError(Exception): # Błąd rekurencji
    pass



def residual_ec(G,Parent,vertex,max_flow):
    while Parent[vertex]!=None:
        for i in range(len(G[Parent[vertex]])):
            if G[Parent[vertex]][i][0]==vertex:
                G[Parent[vertex]][i][1]=0
                break
        for i in range(len(G[vertex])):
            if G[vertex][i][0]==Parent[vertex]:
                G[vertex][i][1]=1
                break
        vertex = Parent[vertex]

def edge_coherence(my_graph,s):
    #return len(min(my_graph.change_representation(0, len(my_graph.edges)-1),key=len)), "Edge Coherence"
    def BFS_list(G,s,t):     # ALgorytm BFS reprezentacja listy sąsiedztwa złożoność(V+E)
        nonlocal max_flow
        flow = float('inf')
        Q=deque([]) 
        PARENT = [None]*len(G)
        VISITED = [False]*len(G)
        VISITED[s] = True
        Q.append(s)
        while len(Q)!=0:
            vertex1=Q.popleft()
            for edge in G[vertex1]:
                neighbour = edge[0]
                if edge[1] > 0 and VISITED[neighbour] == False:
                    PARENT[neighbour] = vertex1 
                    flow = flow if flow < edge[1] else edge[1]
                    if neighbour == t:
                        residual_ec(G,PARENT,neighbour,flow)
    
                        max_flow+=flow
                        return True
                    VISITED[neighbour] = True
                    Q.append(neighbour)


        return False

    
    G = my_graph.change_representation(0, len(my_graph.edges)-1)
    s = s-1
    min_flow = float('inf')
    for t in range(1,len(G)):
        max_flow = 0
        graph_copy = deepcopy(G)
        while BFS_list(graph_copy,s,t):
            continue
        if max_flow < min_flow:
            min_flow = max_flow
    return min_flow, "Edmonds-Karp"
