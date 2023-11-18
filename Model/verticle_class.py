class Verticle:  # Klasa wierzchołka przechowuje korzeń i rodzica
    def __init__(self,parent = None):
        self.root = self
        self.parent = parent

    def find(self):
        if self.parent == None:
            return self.root
        else:
            return self.parent.find()
        