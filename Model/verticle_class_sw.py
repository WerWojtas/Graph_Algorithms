import sys
sys.path.append("C:\\Users\\weron\\OneDrive\\Pulpit\\Grafowe")


class Verticle1:  
  def __init__(self,name):
    self.edges = {}    # słownik  mapujący wierzchołki do których są krawędzie na ich wagi
    self.name = name

  def addEdge( self, to, weight):
    self.edges[to] = self.edges.get(to,0) + weight  # dodaj krawędź do zadanego wierzchołka
                                                    # o zadanej wadze; a jeśli taka krawędź
                                                    # istnieje, to dodaj do niej wagę

  def delEdge( self, to ):
    del self.edges[to]   