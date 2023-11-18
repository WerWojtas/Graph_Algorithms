import os
import sys
sys.path.append("C:\\Users\\weron\\OneDrive\\Pulpit\\Grafowe")
from Model.dimacs import loadDirectedWeightedGraph
from ford_fulkerson import ford_fulkerson
from edmonds import edmonds_karp
from  Model.graph_class import Graph


def check_solution():  # Templatka do sprawdzania zadań
    folder_path = 'C:\\Users\\weron\\OneDrive\\Pulpit\\Grafowe\\Tests\\lab2 TESTY'
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        for file in files:
                print(file)
                file_path = os.path.join(folder_path,file)
                with open(file_path,"r") as G:
                        V,edges,sol = loadDirectedWeightedGraph(G)
                        my_graph = Graph(V,edges)
                        my_sol = edmonds_karp(my_graph,1,my_graph.verticles)
                        if my_sol == int(sol):
                            print("OK")
                        else:
                            print("WRONG",sol,my_sol)

check_solution()
             
                     


