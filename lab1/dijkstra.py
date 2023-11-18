from queue import PriorityQueue
import sys
sys.path.append("C:\\Users\\weron\\OneDrive\\Pulpit\\Grafowe")
from Model.graph_class import Graph

def Dijkstra(G,args): # Algorytm a'la Dijkstra z wykorzystaniem kolejki priorytetowej
    s = args[0] -1
    t = args[1] -1
    my_graph = G.change_representation(0,len(G.edges)-1)    
    distance=[0]*len(my_graph)
    visited=[False]*len(my_graph)
    Q=PriorityQueue()              
    distance[s]=0                      
    Q.put((-10**10,s))         
    while not Q.empty():
        dist,vertex=Q.get()
        dist = -dist
        for edge in my_graph[vertex]:
            neighbour = edge[0]
            if visited[neighbour]==False and distance[neighbour]<min(dist,edge[1]):
                distance[neighbour]=min(dist,edge[1])
                Q.put((-distance[neighbour],neighbour))
        visited[vertex]=True
    
    return distance[t], "Dijkstra"

