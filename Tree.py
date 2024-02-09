from GraphLib import *

class DFSTree:
    def __init__(self, graph):
        self.vertexSet = graph.vertexSet
        self.edgeSet = []
        self.constructDFSTree()

    def constructDFSTree(self):
        root = self.vertexSet[0]
        treeVertecies = [root]
        self.search(root, treeVertecies)
    
    def search(self, root, treeVertecies):
        for vertex in root.neighbors:
            if vertex not in treeVertecies:
                treeVertecies.append(vertex)
                self.edgeSet.append(Edge(root,vertex))
                self.search(vertex, treeVertecies)
    
    def printTree(self):
        for vertex in self.vertexSet:
            print(f"{vertex.name} ")
        for edge in self.edgeSet:
            print(f"{edge.v1.name}, {edge.v2.name}")

class BFSTree:
    def __init__(self, graph):
        self.vertexSet = graph.vertexSet
        self.edgeSet = []
        self.constructBFSTree()

    def constructBFSTree(self):
        root = self.vertexSet[0]
        treeVertecies = [root]
        self.search(root, treeVertecies)
    
    def search(self, root, treeVertecies):
        addedVertecies = []
        for vertex in root.neighbors:
            if vertex not in treeVertecies:
                treeVertecies.append(vertex)
                addedVertecies.append(vertex)
                self.edgeSet.append(Edge(root, vertex))
        
        for vertex in addedVertecies:
            self.search(vertex, treeVertecies)

    def printTree(self):
        for vertex in self.vertexSet:
            print(f"{vertex.name} ")
        for edge in self.edgeSet:
            print(f"{edge.v1.name}, {edge.v2.name}")



            


            