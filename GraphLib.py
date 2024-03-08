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
    
    def toString(self):
        return f"<{self.v1.name}, {self.v2.name}>"

    def __eq__(self, edge):
        return (self.v1 == edge.v1 and self.v2 == edge.v2) or (self.v1 == edge.v2 
            and self.v2 == edge.v1)

    def __hash__(self):
        vertecies = (hash(self.v1), hash(self.v2))
        return hash(tuple(sorted(vertecies)))
class PathConstructor:
    def __init__(self, start):
        self.start = start
        self.current = start
        self.pathAsVertecies = [start]
        self.pathAsEdges = []
    
    def add(self, edge):
        if edge.v1 != self.current:
            print(f"Edge is not at current vertex: {self.current.name}")
            return self
        
        self.pathAsEdges.append(edge)
        self.pathAsVertecies.append(edge.v2)
        self.current = edge.v2
        return self

    def printPath(self):
        string = ""
        i = 0
        while i < len(self.pathAsVertecies):
            if i == len(self.pathAsEdges):
                string += f"{self.pathAsVertecies[i].name}"
            else:
                string += f"{self.pathAsVertecies[i].name} {self.pathAsEdges[i].toString()} "
            i += 1
        print(string)


        

        

        


