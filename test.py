import unittest
from graph import *

class TestGraphColoring(unittest.TestCase):
    def test_graph_coloring(self):
        graph = Graph()
        self.assertTrue(populate_graph(graph, "input.txt"))

        self.assertTrue(graph.color_graph())
class TestGraphColoring2(unittest.TestCase):
    def test_graph_coloring(self):
        graph = Graph()
        self.assertTrue(populate_graph(graph, "input2.txt"))

        self.assertTrue(graph.color_graph())
if __name__ == '__main__':
    unittest.main()



