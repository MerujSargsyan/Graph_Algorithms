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
        self.current = edge.v2
        return self
    def printPath(self):
        string = ""
        for i in range(len(self.pathAsVertecies)):
            if i%2 == 0:
                string += self.pathAsVertecies[i]
            else:
                string += self.pathAsEdges[i]
        print(string)

        

        


