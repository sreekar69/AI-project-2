import unittest
from graph import *

class TestGraphColoring(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName)
        self.test_data_files = ['input.txt', 'input2.txt', 'input3.txt', 'input4.txt', 'input5.txt', 'input6.txt']

    def test_graph_coloring_file1(self):
        data = getData(self.test_data_files[0])
        result = getGraphColoringSolution(data)
        #expected = solution exists
        self.assertTrue(result!=None)

    def test_graph_coloring_file2(self):
        data = getData(self.test_data_files[1])
        result = getGraphColoringSolution(data)
        #expected = solution exists
        self.assertTrue(result!=None)

    def test_graph_coloring_file3(self):
        data = getData(self.test_data_files[2])
        result = getGraphColoringSolution(data)
        #expected = solution exists
        self.assertTrue(result!=None)

    def test_graph_coloring_file4(self):
        data = getData(self.test_data_files[3])
        result = getGraphColoringSolution(data)
        #expected = solution does not exist
        self.assertTrue(result==None)

    def test_graph_coloring_file5(self):
        data = getData(self.test_data_files[4])
        result = getGraphColoringSolution(data)
        #expected = solution exists
        self.assertTrue(result!=None)

    def test_graph_coloring_file6(self):
        data = getData(self.test_data_files[5])
        result = getGraphColoringSolution(data)
        #expected = solution exists
        self.assertTrue(result!=None)

if __name__ == '__main__':
    unittest.main()
