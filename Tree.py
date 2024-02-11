from GraphLib import *

class DFSTree:
    def __init__(self, graph):
        self.vertexSet = sortVertecies(graph.vertexSet)
        self.edgeSet = []
        self.depthMap = {}
        self.constructDFSTree()

    def constructDFSTree(self):
        root = self.vertexSet[0]
        treeVertecies = [root]
        self.depthMap[0] = [root]
        self.search(root, treeVertecies, 0)
    
    def search(self, root, treeVertecies, depth):
        for vertex in sortVertecies(root.neighbors):
            if vertex not in treeVertecies:
                treeVertecies.append(vertex)
                self.edgeSet.append(Edge(root,vertex))
                #if layer is empty, new array is created,
                #otherwise, the array at the level is returned
                self.depthMap.setdefault(depth + 1, []).append(vertex)
                self.search(vertex, treeVertecies, depth + 1)

    def printDepthMap(self):
        for key, value in self.depthMap.items():
            print(f"{key}: {self.printValueArray(value)}")
        print("\n")

    def printValueArray(self, value):
        outputStr = "["
        for vertex in value:
            outputStr += f"{vertex.name}, "
        
        return outputStr + "]"

    def printTree(self):
        for vertex in self.vertexSet:
            print(f"{vertex.name} ")
        for edge in self.edgeSet:
            print(f"{edge.v1.name}, {edge.v2.name}")

class BFSTree:
    def __init__(self, graph):
        self.vertexSet = sortVertecies(graph.vertexSet)
        self.edgeSet = []
        self.depthMap = {}
        self.constructBFSTree()

    def constructBFSTree(self):
        root = self.vertexSet[0]
        treeVertecies = [root]
        self.depthMap[0] = [root]
        self.search(root, treeVertecies, 0)
    
    def search(self, root, treeVertecies, depth):
        addedVertecies = []
        for vertex in sortVertecies(root.neighbors):
            if vertex not in treeVertecies:
                treeVertecies.append(vertex)
                addedVertecies.append(vertex)
                self.edgeSet.append(Edge(root, vertex))
                #if layer is empty, new array is created,
                #otherwise, the array at the level is returned
                self.depthMap.setdefault(depth + 1, []).append(vertex)
                
        
        for vertex in addedVertecies:
            self.search(vertex, treeVertecies, depth + 1)

    def printTree(self):
        for vertex in self.vertexSet:
            print(f"{vertex.name} ")
        for edge in self.edgeSet:
            print(f"{edge.v1.name}, {edge.v2.name}")
    
    def printDepthMap(self):
        for key, value in self.depthMap.items():
            print(f"{key}: {self.printValueArray(value)}")
        print("\n")
    
    def printValueArray(self, value):
        outputStr = "["
        for vertex in value:
            outputStr += f"{vertex.name}, "
        
        return outputStr + "]"
    




            


            