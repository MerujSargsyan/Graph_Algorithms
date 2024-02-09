from GraphLib import *

vertexSet = [Vertex(1), Vertex(2), Vertex(3)]
edgeSet = [Edge(vertexSet[0],vertexSet[1]), 
            Edge(vertexSet[1],vertexSet[2]), 
            Edge(vertexSet[2],vertexSet[0])]
graph = Graph(vertexSet, edgeSet)

print(graph.isBipartite())