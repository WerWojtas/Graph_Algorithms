from verticle_class_sw import Verticle1 as Ve

class Graph:      #  Klasa Grafu, przechowuje liczbę wierzchołków i krawędzi oraz listę krawędzi
    def __init__(self,verticles,edges):
        self.verticles = verticles 
        self.edges = edges

    def change_representation(self,left,right):
        G = [[] for _ in range(self.verticles)]
        for edge in self.edges[left:right+1]:
            G[edge[0]-1].append([edge[1]-1,edge[2]])
            G[edge[1]-1].append([edge[0]-1,edge[2]])
        return G
    
    def change_representation_residual(self):
        G = [[] for _ in range(self.verticles)]
        for edge in self.edges:
            G[edge[0]-1].append([edge[1]-1,edge[2]])
            G[edge[1]-1].append([edge[0]-1,0])
        return G
    
    def sort(self):
        self.edges.sort(key=lambda x: x[2], reverse = True)
        #quick_sort(self.edges,0,len(self.edges)-1

    def change_to_verticles(self):
        G = [ Ve(i) for i in range(self.verticles) ]
        for edge in self.edges:
            G[edge[0]-1].addEdge(edge[1]-1,edge[2])
            G[edge[1]-1].addEdge(edge[0]-1,edge[2])
        return G
