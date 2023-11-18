import os
import time
import sys
import binary_search as bs
sys.path.append("C:\\Users\\weron\\OneDrive\\Pulpit\\Grafowe")
from Model.graph_class import Graph
from find_union import find_edge
from dijkstra import Dijkstra


sys.setrecursionlimit(10000) # Zwiększenie limitu rekurencji
        

def check_solution():  # Templatka do sprawdzania zadań
    folder_path = 'C:\\Users\\weron\\OneDrive\\Pulpit\\Grafowe\\Tests\\lab1 TESTY'
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        print("Który algorytm chcesz wykonać?\n 1 - Find Union\n 2 - Binary Search + BFS\n 3 - Binary Search + DFS\n 4 - Dijkstra\n 5 - Wszystkie(Find Union, Binary + BFS, Dijkstra)\n 0 - Wyjście")
        choice = int(input())
        while choice !=0:
            counter = 0
            time_1 = 0
            time_2 = 0
            time_3 = 0
            s_time = time.process_time()
            for file in files:
                file_path = os.path.join(folder_path,file)
                with open(file_path,"r") as Graph:
                    start_time = time.process_time()
                    my_graph,sol = read_graph(Graph)
                    my_graph.sort()
                    args = (1,2,bs.BFS_list)
                    if choice == 1:
                        my_sol = find_edge(my_graph,args)
                    elif choice == 2:
                        my_sol = bs.binary_search(my_graph,args)
                    elif choice == 3:
                        my_sol = bs.binary_search(my_graph, bs.DFS)
                    elif choice == 4:
                        my_sol = Dijkstra(my_graph,args)
                    elif choice == 5:
                        counter2 = 0
                        my_sol1 = find_edge(my_graph,args)
                        end_time1 = time.process_time()
                        my_sol2 = bs.binary_search(my_graph,args)
                        end_time2 = time.process_time()
                        my_sol3 = Dijkstra(my_graph,args)
                        end_time3 = time.process_time()
                        if my_sol1 == int(sol):
                            counter2 +=1
                            counter +=1
                        if my_sol2 == int(sol):
                            counter2 +=1
                            counter +=1
                        if my_sol3 == int(sol):
                            counter2 +=1
                            counter +=1
                        print(counter2)
                        time_1+=end_time1-start_time
                        time_2+=end_time2-start_time-(end_time1-start_time)
                        time_3+=end_time3-start_time-(end_time2-start_time)
                        print("Plik : ",file,"\n Wynik Find Union:", my_sol1, "Czas: ", round(end_time1-start_time,4), "s\n Wynik Binary + BFS:", my_sol2, "Czas: ", round(end_time2-start_time-(end_time1-start_time),4), "s")
                        print(" Wynik Dijkstra:", my_sol3, "Czas: ", round(end_time3-start_time-(end_time2-start_time),4), "s\n Wynik prawidłowy:", sol, "\n Całkowity wynik: ", counter2, "/3")
                        print("-----------------------------------------------")
                        leng = len(files)*3
                        continue
                    leng = len(files)
                    end_time = time.process_time()
                    if my_sol == int(sol):
                        print("Plik : ",file," Test zaliczony! Czas:", round(end_time - start_time, 4), "s")
                        counter+=1
                    else:
                        print("Plik : ",file," Test niezaliczony! Oczekiwany wynik: ",sol," Uzyskany wynik: ",my_sol)
            e_time = time.process_time()
            print("Czas wykonania wszystkich testów: ",round(e_time - s_time, 4),"s, zaliczonych: ",counter,"/",leng)
            if choice == 5:
                print("Czas wykonania Find Union: ",round(time_1,4),"s\nCzas wykonania Binary + BFS: ",round(time_2,4),"s\nCzas wykonania Dijkstra: ",round(time_3,4),"s")
            print("-----------------------------------------------")
            print("Który algorytm chcesz wykonać?\n 1 - Find Union\n 2 - Binary Search + BFS\n 3 - Binary Search + DFS\n 4 - Dijkstra\n 5 - Wszystkie(Find Union, Binary + DFS, Dijkstra)\n 0 - Wyjście")
            choice = int(input())


def load_graph(graph_path):   # Funkcja wczytująca pojedyczny graf z podanej ścieżki
    with open(graph_path, "r") as Graph:
        my_graph = read_graph(Graph)
        return my_graph


                
def read_graph(graph_file):    # Funkcja wczytująca grafy z pliku, gdzie Graph jest odczytanym plikiem
    my_graph = Graph(0,[])
    lines = graph_file.readlines()
    for line in lines:
        tab = line.split()
        if tab[0] == None:
            return my_graph,sol
        elif tab[0] == 'p':
            my_graph.verticles = int(tab[2])
        elif tab[0] == 'e':
            edge = (int(tab[1]),int(tab[2]),int(tab[3]))
            my_graph.edges.append(edge)
        elif tab[0] == 'c':
            sol = tab[3]
    return my_graph,sol
    

check_solution()
    










    








