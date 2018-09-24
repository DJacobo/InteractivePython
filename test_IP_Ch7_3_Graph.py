import unittest
from IPCh73Graph import Graph, Vertex

class GraphTest(unittest.TestCase):
    def test_create_graph(self):
        self.g = Graph()

    @unittest.skip("WIP")
    def test_add_vertex(self):
        self.g = Graph()
        self.g.addVertex(7)
        self.assertTrue('True', self.g.__contains__(7))

