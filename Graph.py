from Tree import BFSTree
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
    
    def findCyclesAtV(self, length, root):
        try: 
            # swap root to front of list
            index = self.vertexSet.index(root)
            temp = self.vertexSet[0]
            self.vertexSet[0] = root
            self.vertexSet[index] = temp
        except:
            print("vertex not in list")
            return 


        