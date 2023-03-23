import sys
from graph import *

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.colors = []

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = Vertex(v)

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj_list[v1].add_neighbor(self.adj_list[v2])
        self.adj_list[v2].add_neighbor(self.adj_list[v1])

    def set_colors(self, colors):
        self.colors = colors

    def color_graph(self):
        # color each vertex
        for vertex in self.adj_list.values():
            used_colors = set()
            for neighbor in vertex.neighbors:
                if neighbor.color != 0:
                    used_colors.add(neighbor.color)
            for color in self.colors:
                if color not in used_colors:
                    vertex.color = color
                    break
            else:
                return False
        return True

    def __str__(self):
        output = ""
        for vertex in self.adj_list.values():
            output += str(vertex.id) + " : " + str(vertex.color) + "\n"
        return output


class Vertex:
    def __init__(self, v):
        self.id = v
        self.color = 0
        self.neighbors = []

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)




# Return of successive ints representing colors in range 0 to num_colors
def create_colors(num_colors):
    colors = []
    for i in range(1, int(num_colors + 1)):
        colors.append(i)
    return colors


def populate_graph(graph, filename):
    f = open(filename, "r")
    lines = f.readlines()

    num_colors = 0

    for line in lines:
        # Skip comment lines
        if line[0] == "#":
            continue

        # This is the "Colors = n" line
        if num_colors == 0 and len(line) >= 8 and str(line[0:6]).lower() == "colors":
            line = line[6:].lstrip().rstrip()

            if line[0] != "=":
                return False

            try:
                num_colors = int(line[1:])
            except:
                return False

            graph.set_colors(create_colors(num_colors))

        # Once num_colors has been initialized, read vertexes and edges
        elif num_colors > 0:
            vals = line.lstrip().rstrip().split(",")
            if len(vals) != 2:
                return False

            graph.add_edge(vals[0], vals[1])

    return bool(num_colors)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Incorrect arguments. Must provide filename of graph data.")

    graph = Graph()

    if not populate_graph(graph, sys.argv[1]):
        sys.exit("Unable to parse " + str(sys.argv[1]))

    if graph.color_graph():
        print(graph)
    else:
        print("Graph cannot be colored!")

