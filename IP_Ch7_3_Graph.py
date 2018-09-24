# Graph() creates a new, empty graph.
# addVertex(vert) adds an instance of Vertex to the graph.
# addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
# addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
# getVertex(vertKey) finds the vertex in the graph named vertKey.
# getVertices() returns the list of all vertices in the graph.
# in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + ' is connected to: ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    
    def getVertices(self):
        return self.vertList.keys

    def __iter__(self):
        return iter(self.vertList.values())

    def __str__(self):
        for v in self:
            for w in v.getConnections():
                print("( %s , %s )" % (v.getId(), w.getId()))

# g = Graph()
# for i in range(6):
#     g.addVertex(i)
# g.addEdge(0,1,5)
# g.addEdge(0,5,2)
# g.addEdge(1,2,4)
# g.addEdge(2,3,9)
# g.addEdge(3,4,7)
# g.addEdge(3,5,3)
# g.addEdge(4,0,1)
# g.addEdge(5,4,8)
# g.addEdge(5,2,1)
# for v in g:
#     for w in v.getConnections():
#         print("( %s , %s )" % (v.getId(), w.getId()))