import sys


class Vertex:
    def __init__(self, node_id, colors):
        self.id = node_id
        self.color = None  # Only set once definite
        self.colors_remain = colors.copy()  # All possible remaining colors
        self.adj = set()  # Track nodes this one is adjacent to

    """
    Set the color for this vertex and remove all other colors from its
    colors_remain list.
    """

    def set_color(self, color):
        self.color = color
        self.colors_remain = [color]

    def add_neighbor(self, neighbor):
        self.adj.add(neighbor)

    def __str__(self):
        return str(self.id) + " : " + str(self.color)


class Graph:
    def __init__(self):
        self.nodes = {}
        self.colors = None  # List of all possible colors

    def set_colors(self, colors):
        self.colors = colors

    def add_edge(self, src, dst):
        # Create vertex objects if they don't already exist
        if src not in self.nodes:
            self.nodes[src] = Vertex(src, self.colors)
        if dst not in self.nodes:
            self.nodes[dst] = Vertex(dst, self.colors)

        # Create edges
        self.nodes[src].add_neighbor(self.nodes[dst])
        self.nodes[dst].add_neighbor(self.nodes[src])

    def __str__(self):
        s = "Vertex ID : Color\n"
        for v in self.nodes:
            s += str(self.nodes[v])
            s += "\n"
        return s

    """
    Returns the least constraining value (color) for vertex v.
    """

    def lcv(self, v):
        lcv = None
        min_num_affected = float('inf')

        for c in v.colors_remain:
            num_affected = 0
            for u in v.adj:
                if c in u.colors_remain:
                    num_affected += 1
            if num_affected < min_num_affected:
                lcv = c
                min_num_affected = num_affected

        return lcv

    """
    Returns the vertex with the minimum remaining possible colors. Ties are
    broken based on the vertex with the least constraints.
    uncolored: list of vertexes yet to be colored
    """

    def mrv(self, uncolored):
        # Most constrained variable
        mcv = None

        for v in uncolored:
            # Get vertex obj of v
            v = self.nodes[v]

            # If this vertex has already been colored, continue
            if v.color != None:
                continue

            if mcv == None:
                mcv = v
            elif len(v.colors_remain) < len(mcv.colors_remain):
                mcv = v
            elif len(v.colors_remain) == len(mcv.colors_remain):
                if len(v.adj) > len(mcv.adj):
                    mcv = v

        return mcv

    def rm_inconsistent_vals(self, v, u):
        removed = False

        i = 0
        n = len(v.colors_remain)
        while i < n:
            cx = v.colors_remain[i]

            # Is cx the only remaining color for u?
            if len(u.colors_remain) == 1 and u.colors_remain[0] == cx:
                v.colors_remain.remove(cx)
                n -= 1
                removed = True
            i += 1

        return removed

    """
    Add every arc (2-tuple) of the form (v,U) to the queue such that v is an uncolored node.
    uncolored: list of unoclored nodes left in the graph
    """

    def create_arcs(self, uncolored):
        queue = []

        for v in uncolored:
            v = self.nodes[v]
            for u in v.adj:
                queue.append((v.id, u.id))

        return queue

    def ac3(self, uncolored):
        queue = self.create_arcs(uncolored)
        while queue:
            arc = queue.pop(0)
            v = self.nodes[arc[0]]
            u = self.nodes[arc[1]]
            if self.rm_inconsistent_vals(v, u):
                for k in v.adj:
                    queue.append((k.id, v.id))

    """
    Function colors graph. Returns True on sucess, False otherwise.
    """

    def color_graph(self):
        uncolored = list(self.nodes.keys())

        while v := self.mrv(uncolored):
            lcv = self.lcv(v)

            # If lcv does not return a color, graph cannot be colored
            if lcv == None:
                return False

            v.set_color(lcv)
            uncolored.remove(v.id)
            self.ac3(uncolored)

        return True

