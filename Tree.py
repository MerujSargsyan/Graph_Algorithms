from GraphLib import *

class Tree:
    def __init__(self, graph):
        self.vertexSet = graph.vertexSet
        self.edgeSet = []
        self.constructBasicTree()

    def constructBasicTree(self):
        root = self.vertexSet[0]
        current = root
        treeVertecies = [root]
        self.search(current, treeVertecies)
    
    def search(self, root, countedVertecies):
        for vertex in root.neighbors:
            if vertex not in countedVertecies:
                countedVertecies.append(vertex)
                self.edgeSet.append(Edge(root,vertex))
                self.search(vertex, countedVertecies)
    
    def printTree(self):
        for vertex in self.vertexSet:
            print(f"{vertex.name} ")
        for edge in self.edgeSet:
            print(f"{edge.v1.name}, {edge.v2.name}")


            


            