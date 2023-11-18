import sys
sys.path.append("C:\\Users\\weron\\OneDrive\\Pulpit\\Grafowe")
from Model.verticle_class import Verticle

def union(verticle1,verticle2,s,t): # Funkcja union operująca na wierzchołkach, przystosowana do szukania s i t jako korzeni
    root1 = verticle1.find()
    root2 = verticle2.find()
    if root1.root == root2.root:
        return False
    if (root2 == s and root1 == t) or (root1 == s and root2 == t):
        return True
    if root2 == s or root2 == t:
        root1.parent = root2
    else:
        root2.parent = root1
    return False

def find_edge(Graph,args):      # Funkcja wykorzystująca find_union do znalezienia krawędzi
    Graph.sort()
    s = args[0]
    t = args[1]
    Verticles = [Verticle() for _ in range(Graph.verticles)]
    for v1,v2,c in Graph.edges:
        if union(Verticles[v1-1],Verticles[v2-1],Verticles[s-1],Verticles[t-1]):
             return c, "Find-union"
   
