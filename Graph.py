from Tree import DFSTree
from GraphLib import *

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

        