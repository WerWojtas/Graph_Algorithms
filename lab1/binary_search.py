from collections import deque

class RecursionTimeoutError(Exception): # Błąd rekurencji
    pass


def DFS(G,s,t,max_depth,depth = 0):  # DFS z zabezpieczeniem rekurencji
    Visited = [0] * len(G)
    s = s-1
    t = t-1
    
    def DFS_visit(G, vertex, t, max_depth, depth):
        if depth > max_depth:
            raise RecursionTimeoutError("Przekroczono maksymalną głębokość rekurencji")
        Visited[vertex] = 1
        if vertex == t:
            return True
        for edge in G[vertex]:
            neighbour = edge[0]
            if Visited[neighbour] == 0:
                if DFS_visit(G, edge[0], t, max_depth, depth+1):
                    return True
        return False

    return DFS_visit(G, s, t, max_depth, depth)

def BFS_list(G,s,t,max_depth):     # ALgorytm BFS reprezentacja listy sąsiedztwa złożoność(V+E)
    s = s-1
    t = t-1
    Q=deque([]) 
    VISITED=[0]*len(G)
    Q.append(s)
    VISITED[s]=1
    while len(Q)!=0:
        vertex1=Q.popleft()
        for edge in G[vertex1]:
            neighbour = edge[0]
            if neighbour==t:
                return True
            if VISITED[neighbour]==0:
                Q.append(neighbour)
                VISITED[neighbour]=1
    return False

def binary_search_previous(G,left,right,function,power = 1,max_depth = 1000): # Funkcja wyszukująca krawędź binarnie z zabezpieczeniem rekurencji
    def recursive_binary_search(left, right, power):
        if power > max_depth:
            raise RecursionTimeoutError("Przekroczono maksymalną głębokość rekurencji")
        diff = (left + right) // (2 ** power)
        if diff == 0:
            return G.edges[right][2]
        right_true = right - diff
        G_neighbours = G.change_representation(left, right_true)
        if function(G_neighbours, 1, 2, max_depth):
            return recursive_binary_search(left, right_true, power)
        else:
            return recursive_binary_search(left, right, power+1)

    try:
        return recursive_binary_search(left, right, power)
    except RecursionTimeoutError as e:
        print("Błąd!! Rekurencja przekroczyła maksymalną domyślną głębokość (1000). Algorytm BFS działa w tym przypadku dużo lepiej.")

def binary_search(G, args):
    G.sort()
    s = args[0]
    t = args[1]
    func = args[2]
    left, right = 0, len(G.edges)-1
    
    while left <= right:
        mid = (left + right) // 2
        my_graph = G.change_representation(0, mid)
        if func(my_graph, s, t, 1000):
            right = mid-1
            low = mid
        else:
            left = mid + 1
    return G.edges[low][2], "Binary search"