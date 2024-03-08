from Tree import DFSTree
from GraphLib import *
import random

class Graph:
    def __init__(self, vertexSet, edgeSet):
        self.vertexSet = vertexSet
        self.edgeSet = edgeSet
    
    def isBipartite(self):
        groupA = []
        groupB = []

        #populates groupA from groupB
        for vertex in self.vertexSet:
            if not groupA:
                groupA.append(vertex)
                continue
            
            repCountA = 0
            for vertexA in groupA:
                if vertexA.hasNeighbor(vertex):
                    break
                else:
                    repCountA += 1

            if repCountA == len(groupA):
                groupA.append(vertex)
                continue            
            
            for vertexB in groupB:
                if vertexB.hasNeighbor(vertex):
                    return False

            groupB.append(vertex)        
        return True
    
    def findPath(self, v1, v2):
        tree = DFSTree(self)
        return tree.findPath(v1, v2)

    def nextVertex(self, v, currentPath, goal):
        if currentPath.current == goal:
            return currentPath

    def toString(self):
        outputEdges = ""
        outputVertecies = ""
        for e in self.edgeSet:
            outputEdges += e.toString() + " "
        for v in self.vertexSet:
            outputVertecies += str(v.name) + " "
        return outputVertecies + " " + outputEdges

# creates a randomly generated graph by taking size of a and b and
# making edges between vertecies based on strength 
# strength: 1 - a+b (maximum number of edges to generate per vertex)
def createSimpleGraph(n, strength):
    vertexSet = []
    edgeSet = set()
    for i in range(n):
        vertexSet.add(Vertex(i))
    
    for vertex in vertexSet:
        # new set that doesn't include the current vertex
        validSet = vertexSet.copy().remove(vertex)
        for i in range(strength):
            edgeSet.add(Edge(vertex, random.randint(0, range(validSet))))
    
    return Graph(vertexSet, edgeSet)


    

    

        