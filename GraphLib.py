class Vertex:
    def __init__(self, name):
        self.name = name
        self.value = int(name)
        self.neighbors = []

    def addNeighbor(self, neighborV):
        self.neighbors.append(neighborV)

    def hasNeighbor(self, v):
        return v in self.neighbors

def sortVertecies(vertecies):
    #returns the vertecies from smallest to largest
    return sorted(vertecies, key=lambda x: x.value)

class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        v1.addNeighbor(v2)
        v2.addNeighbor(v1)

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

class PathConstructor:
    def __init__(self, start):
        self.start = start
        self.current = start
        self.pathAsVertecies = [start]
        self.pathAsEdges = []
    
    def add(self, edge):
        if edge.v1 != self.current:
            print(f"Edge is not at current vertex: {self.current.name}")
            return
        
        self.pathAsEdges.append(edge)
        self.pathAsVertecies.append(edge.v2)

        

        


