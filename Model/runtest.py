import os
import sys
import time
sys.path.append("C:\\Users\\weron\\OneDrive\\Pulpit\\Grafowe")
import dimacs
from graph_class import Graph
import lab1.binary_search as bs
from lab1.dijkstra import Dijkstra
from lab1.find_union import find_edge
from lab2.edmonds import edmonds_karp
from lab2.ford_fulkerson import ford_fulkerson


class Test():
    def __init__(self,functions,lab_no):
        self.functions = functions
        self.lab_no = lab_no
        if lab_no == 1:
            self.load_graph = dimacs.loadWeightedGraph
            self.args = (1,2, bs.BFS_list)
        if lab_no == 2:
            self.load_graph = dimacs.loadDirectedWeightedGraph
            self.args = 1

    def runtest(self):
        folder_path = 'C:\\Users\\weron\\OneDrive\\Pulpit\\Grafowe\\Tests\\lab'+str(self.lab_no)+ ' TESTS'
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            files = os.listdir(folder_path)
            leng = len(self.functions)
            times = [0]*leng
            names = [0]*leng
            s_time = time.process_time()
            count = 0
            flag = 0
            for file in files:
                print("File {}: ",file)
                file_path = os.path.join(folder_path,file)
                with open(file_path,"r") as G:
                    counter = 0
                    V,edges,sol = self.load_graph(G)
                    my_graph = Graph(V,edges)
                    for i in range(leng):
                        flag+=1
                        func = self.functions[i]
                        start = time.process_time()
                        my_sol, name = func(my_graph,self.args)
                        if count == 0:
                            names[i] = name
                        end = time.process_time()
                        times[i]+=(end - start)
                        if my_sol == int(sol):
                            counter+=1
                            print("Function: {} - Passed, Time: {:.3f} s".format(name, end-start))
                        else:
                            print("Function: {} - Wrong result, Your result: {}, Corect result: {}".format(name, my_sol, sol))
                    print("Result: {}/{}".format(counter,leng))
                    print("------------------------------------------------------")
                count+=counter
            e_time = time.process_time()
            print("Final result: {}/{}, Final time: {:.3f} s".format(count,flag,e_time-s_time))
            for i in range(leng):
                print("Function: {}, Final time {:.3f} s".format(names[i],times[i]))


test = Test([bs.binary_search,Dijkstra,find_edge],1)
test.runtest()




