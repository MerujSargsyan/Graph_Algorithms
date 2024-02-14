from GraphLib import *
from Tree import *
from Graph import Graph

vertexSet = [Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5), 
            Vertex(6)]
edgeSet = [Edge(vertexSet[0],vertexSet[1]), 
            Edge(vertexSet[1],vertexSet[2]), 
            Edge(vertexSet[1],vertexSet[5]),
            Edge(vertexSet[1],vertexSet[4]),
            Edge(vertexSet[2],vertexSet[3]),
            Edge(vertexSet[3],vertexSet[4])]
graph = Graph(vertexSet, edgeSet)
tree = BFSTree(graph)
tree2 = DFSTree(graph)

