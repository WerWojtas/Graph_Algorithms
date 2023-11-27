import copy
import sys
sys.path.append("C:\\Users\\weron\\OneDrive\\Pulpit\\Grafowe")
from time import sleep

merged = [i for i in range(20)]

def stoer_wagner(G,arg):
    verticles = G.verticles
    G = G.change_to_verticles()
    min_cut = float('inf')

    while verticles > 1:
        my_graph = copy.deepcopy(G)
        vert1,weight,merged = merge(my_graph, verticles)

        for key in G[vert1].edges.keys():
            if key in merged:
                vert2 = key
                break
        if len(merged) == 0:
            vert2 = 0
        G = merge_2(G, vert1,vert2)
        verticles -= 1
        if weight < min_cut:
            min_cut = weight

    return min_cut, "stoer_wagner"




def merge(G, vertices):
    merged = []

    while vertices > 2:
        merge_vert, _ = max(G[0].edges.items(), key=lambda x: x[1])
        merged.append(merge_vert)

        G[merge_vert].delEdge(0)
        G[0].delEdge(merge_vert)
        vertices -= 1
        for edge_to, weight in G[merge_vert].edges.items():
            G[0].addEdge(edge_to, weight)
            G[edge_to].delEdge(merge_vert)
            G[edge_to].addEdge(0, weight)




    for edge_to, weight in G[0].edges.items():
        return edge_to,weight,merged


def merge_2(G, vert1,vert2):
    G[vert2].delEdge(vert1)
    G[vert1].delEdge(vert2)
    for edge_to, weight in G[vert2].edges.items():
        G[vert1].addEdge(edge_to, weight)
        G[edge_to].delEdge(vert2)   
        G[edge_to].addEdge(vert1, weight)
    
    return G
    




def G_print(G,vert):
    for key, value in G[vert].edges.items():
        print(vert, key, value)

    




